import requests

class currency_service:

	# Call API to get latest rates - https://currencylayer.com/quickstart 
	def get_rates():

		data = requests.get('http://www.apilayer.net/api/live?access_key=88b5656f48dc23632ce1e4ce7150bd63&currencies=USD,GBP,EUR&format=1').json()

		return data

	def get_rate(currency1, currency2):

		data = currency_service.get_rates()

		currency1_rate = 0

		if currency1.lower() == 'gbp':
			currency1_rate = data['quotes']['USDGBP']
		elif currency1.lower() == 'eur':
			currency1_rate = data['quotes']['USDEUR']
		elif currency1.lower() == 'usd':
			currency1_rate = data['quotes']['USDUSD']

		currency2_rate = 0

		if currency2.lower() == 'gbp':
			currency2_rate = data['quotes']['USDGBP']
		elif currency2.lower() == 'eur':
			currency2_rate = data['quotes']['USDEUR']
		elif currency2.lower() == 'usd':
			currency2_rate = data['quotes']['USDUSD']

		if currency1_rate > currency2_rate:
			return currency2_rate;
		else:
			return 1 / currency1_rate;