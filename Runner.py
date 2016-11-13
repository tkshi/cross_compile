# -*- coding: utf-8 -*-
import sys
from Twitter import *
from Gmail import *
from Excel import *
from Register import run
from Error import *
from Util import *
import os

twitterList = getSheet(fileName="./uploads/twitter.xls",sheetName="Accounts")
googleList = getSheet(fileName="./uploads/gmail.xls",sheetName="Accounts")

# def run(TWITTER_ID,TWITTER_PASS,TWITTER_EMAIL,
# 	GMAIL_ADRESS,GMAIL_PASS,PHONE_NUMBER):
# 	return True

def start(APP_IP='36.55.241.31',TWITTER_SHEET_PATH="./uploads/twitter.xls",GOOGLE_SHEET_PATH="./uploads/gmail.xls",TRY_COUNT=10,PHONE_TRY_COUNT=5):
	os.chmod(TWITTER_SHEET_PATH, 0777)
	os.chmod(GOOGLE_SHEET_PATH, 0777)
	twitterList = getSheet(fileName=TWITTER_SHEET_PATH,sheetName="Accounts")
	googleList = getSheet(fileName=GOOGLE_SHEET_PATH,sheetName="Accounts")
	register_count = 0
	for gi,grow in enumerate(googleList):
		if (gi == PHONE_TRY_COUNT):
			raise PhoneNumberInvalidError()
		gmail_id = grow[0]
		gmail_pass =grow[1]
		phone_number = grow[2]
		status = grow[3] if len(grow) == 4 else ''
		if status == 'error' or status == 'done' or grow[0].find('@') == -1:
			continue
	 	try:
			for i,trow in enumerate(twitterList):
				# if( countLengthRow(rows=twitterList,length=4) == TRY_COUNT):
				# 	raise OverTryCountError()

				if len(trow) == 4 and trow[3] != '':
					continue
				twitter_id = trow[0]
				twitter_pass = trow[1]
				twitter_email = trow[2]
				try:
					run(TWITTER_ID=twitter_id,TWITTER_PASS=twitter_pass,TWITTER_EMAIL=twitter_email,
		GMAIL_ADRESS=gmail_id,GMAIL_PASS=gmail_pass,PHONE_NUMBER=phone_number,APP_IP=APP_IP)
					register_count = register_count + 1
					if(register_count == TRY_COUNT):
						raise OverTryCountError()
					try:
						trow[3] = "done"
					except IndexError:
						trow.append("done")
				except (TwitterLoginError,AlreadyAddedPhoneNumber,CannotRegisterYetError) as e:
					if(isinstance(e,TwitterLoginError)):
						try:
							trow[3] = 'error'
						except (IndexError) as e:
							trow.append('error')
					elif(isinstance(e,AlreadyAddedPhoneNumber)):
						try:
							trow[3] = "done"
						except (IndexError) as e:
							trow.append("done")
						register_count = register_count + 1
						if(register_count == TRY_COUNT):
							raise OverTryCountError()
					elif(isinstance(e,CannotRegisterYetError)):

						try:
							trow[3] = ''
						except (IndexError) as e:
							trow.append('')
				writeSheet(fileName=TWITTER_SHEET_PATH,sheetName='Accounts',rows=twitterList)
		except PhoneNumberInvalidError:
			try:
				grow[3] = 'error'
			except IndexError:
				grow.append('error')
		writeSheet(fileName=GOOGLE_SHEET_PATH,sheetName='Accounts',rows=googleList)


if __name__ == '__main__':
	start(APP_IP='182.163.60.59',TWITTER_SHEET_PATH="./uploads/twitter.xls",GOOGLE_SHEET_PATH="./uploads/gmail.xls",TRY_COUNT=1)


# writeSheet(fileName="./uploads/gmail_out.xls",sheetName='Accounts',rows=gmailResult)
# writeSheet(fileName="./uploads/twitter_out.xls",sheetName='Accounts',rows=twitterResult)
