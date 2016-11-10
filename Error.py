class TwitterLoginError(Exception):
	def __init__(self):
		pass
	def __str__(self):
		pass

class PhoneNumberInvalidError(Exception):
	def __init__(self):
		pass
	def __str__(self):
		pass

class AlreadyAddedPhoneNumber(Exception):
	def __init__(self):
		pass
	def __str__(self):
		pass

class CannotRegisterYetError(Exception):
	def __init__(self):
		pass
	def __str__(self):
		pass
class OverTryCountError(Exception):
	def __init__(self):
		pass
	def __str__(self):
		pass


if __name__ == '__main__':
	raise TwitterLoginError()
