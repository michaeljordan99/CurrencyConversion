class validation_service:

	def amount_is_valid(amount):

		try:
			float(amount)
			return True
		except ValueError:
			return False

	def currency_is_valid(currency):

		if currency.lower() == 'usd' or currency.lower() == 'eur' or currency.lower() == 'gbp':
			return True
		return False
