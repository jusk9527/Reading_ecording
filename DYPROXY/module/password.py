"""
	this module is for producing a valid password
	that for Cipher to encode and decode the data flow.
"""
########################################################
# 随机产生一个用于提供加解密映射关系的 256 byte 数组
########################################################


import random
import base64

PASSWORD_LENGTH = 256
IDENTITY_PASSWORD = bytearray(range(256))


# 密码不合法错误
class InvalidPasswordError(Exception):
	"""Error: Invalid Password"""



# 定义数组长度 256
# len = length
def validatePassword(password):
	return len(password) == PASSWORD_LENGTH and len(set(password)) == PASSWORD_LENGTH


# load
def loadsPassword(passwordString):
	try:
		password = base64.urlsafe_b64decode(passwordString.encode('utf8', errors='strict'))
		password = bytearray(password)
	except:
		raise InvalidPasswordError

	if not validatePassword(password):
		raise InvalidPasswordError

	return password


# dump
def dumpsPassword(password):
	if not validatePassword(password):
		raise InvalidPasswordError

	return base64.urlsafe_b64encode(password).decode('utf8', errors='strict')


# random
def randomPassword():
	password = IDENTITY_PASSWORD.copy()
	random.shuffle(password)
	return password


password = randomPassword()

base64_password = dumpsPassword(password)

# byte--->base64
# print(base64_password)

# # base46--->byte
# print(loadsPassword(base64_password))
