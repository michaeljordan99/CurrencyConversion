from flask import Flask, jsonify
from currency_service import currency_service

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
@app.route('/rate/<string:currency1>/to/<string:currency2>')
def currency_rate(currency1, currency2):

	rate = currency_service.get_rate(currency1, currency2)

	if rate == 0:
		return jsonify({'error': 'Currency not found'})

	return jsonify(
		{	
			'from': '{}'.format(currency1), 
			'to': '{}'.format(currency2),
			'rate': '{}'.format(rate)
		})

# GET /convert/currency1/amount/to/currency2
@app.route('/convert/<string:currency1>/<float:amount>/to/<string:currency2>')
def currency_convert(currency1, amount, currency2):

	rate = currency_service.get_rate(currency1, currency2)

	if rate == 0:
		return jsonify({'error': 'Currency not found'})

	converted_amount = round(amount * rate, 2)

	return jsonify(
		{	
			'from': '{}'.format(currency1), 
			'from_amount':'{}'.format(amount),
			'to': '{}'.format(currency2),
			'converted_amount': '{}'.format(converted_amount),
			'rate': '{}'.format(rate)
		})


