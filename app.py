from flask import Flask, jsonify
from currency_service import currency_service
from validation_service import validation_service

app = Flask(__name__)

@app.route('/hello')
def hello():
    """Simple example of an API endpoint"""
    return jsonify({'message': 'ohai'})


@app.route('/hello/<string:name>')
def hello_name(name):
    """Simple example using an URL parameter"""
    return jsonify({'message': 'ohai {}'.format(name)})

# Discogs Marketplace Squad - currency conversion endpoints

# GET /rate/currency1/to/currency2
@app.route('/rate/<string:currency1>/to/<string:currency2>', methods = ['GET'])
def currency_rate(currency1, currency2):

	if not validation_service.currency_is_valid(currency1) or not validation_service.currency_is_valid(currency2):
		response = jsonify({'error': 'Currency not supported'})
		response.status_code = 400
		return response

	rate = currency_service.get_rate(currency1, currency2)

	if rate == 0:
		return jsonify({'error': 'Currency not found'})

	response = jsonify(
				{	
					'from': '{}'.format(currency1), 
					'to': '{}'.format(currency2),
					'rate': '{}'.format(rate)
				})

	return response

# GET /convert/currency1/amount/to/currency2
@app.route('/convert/<string:currency1>/<float:amount>/to/<string:currency2>', methods = ['GET'])
def currency_convert(currency1, amount, currency2):

	if not validation_service.amount_is_valid(amount):
		response = jsonify({'error': 'Amount is not valid'})
		response.status_code = 400
		return response

	if not validation_service.currency_is_valid(currency1) or not validation_service.currency_is_valid(currency2):
		response = jsonify({'error': 'Currency not supported'})
		response.status_code = 400
		return response

	rate = currency_service.get_rate(currency1, currency2)

	converted_amount = round(amount * rate, 2)

	response = jsonify(
				{	
					'from': '{}'.format(currency1), 
					'from_amount':'{}'.format(amount),
					'to': '{}'.format(currency2),
					'converted_amount': '{}'.format(converted_amount),
					'rate': '{}'.format(rate)
				})

	return response


