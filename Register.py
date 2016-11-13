from Gmail import *
from SocialLogin import *
from Twitter import *
from Error import *



def run(TWITTER_ID = "askaniyagavril6",TWITTER_PASS = "O9FncJiCO1",TWITTER_EMAIL = "IzabellaTihonova1983@list.ru",
GMAIL_ADRESS = "frabro568@gmail.com",GMAIL_PASS = "ndagmabry9",PHONE_NUMBER = "(830) 308-7334",APP_IP='36.55.241.31'):

	tw = Twitter(twitter_id=TWITTER_ID,twitter_pass=TWITTER_PASS,twitter_email=TWITTER_EMAIL)
	tw.setLangage()
	tw_driver = tw.getDriver()
	try:
		tw.setPhone(phone_number=PHONE_NUMBER)
	except AlreadyAddedPhoneNumber:
		sl = SocialLogin(driver=tw_driver,app_ip=APP_IP)
		sl.twitterLogin()
		tw.close()
		raise AlreadyAddedPhoneNumber()
	gm = Gmail(gmail_adress=GMAIL_ADRESS,gmail_pass=GMAIL_PASS)
	pin_code = gm.getPinCode()
	sleep(5)
	tw.setPINKey(pin_code=pin_code)
	if(tw.checkMobile() == False):
		tw.close()
		gm.close()
		raise PhoneNumberInvalidError()
	driver = tw.getDriver()
	sl = SocialLogin(driver=driver,app_ip=APP_IP)
	sl.twitterLogin()
	tw.close()
	gm.close()
if __name__ == '__main__':
	raise run()
