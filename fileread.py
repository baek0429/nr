import codecs


# get read filename from same directory and  returns url(string)
def getReservationInfo(fileName):
	# file read
	try:
		f = codecs.open(fileName,'r',encoding='utf8')
		contents = f.read()
		infoArray = [x.strip() for x in contents.split(',')]
		courtNumber = infoArray[0]
		timeID = infoArray[1]
		print("court number :" +  courtNumber + ", TimeID:"+ timeID)
		return infoArray
	except Exception as e:
		print e

def getLoginInfo(fileName):
	# file read
	try:
		f = codecs.open(fileName,'r',encoding='utf8')
		contents = f.read()
		infoArray = [x.strip() for x in contents.split(',')]
		print "Reservation ID: " + infoArray[1]
		return infoArray
	except Exception as e:
		print e


if __name__ == "__main__":
	getReservationInfo('info.txt')
