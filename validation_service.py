class validation_service:

	def amount_is_valid(amount):

		try:
			float(amount)
			return True
		except ValueError:
			return False