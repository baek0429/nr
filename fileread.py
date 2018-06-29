import codecs

# Court Number Array
courtNumbers = {
	'3' : '2633373',
	'4' : '2652587',
	'5' : '2652589',
	'6' : '2652590',
	'7' : '2652591',
	'8' : '2652592',}

# dictionary mirroring (change court and number)
courtNumbers = {y:x for x,y in courtNumbers.iteritems()}

# get read filename from same directory and  returns url(string)
def getReservationInfo(fileName):
	# file read
	try:
		f = codecs.open(fileName,'r',encoding='utf8')
		contents = f.read()
		infoArray = [x.strip() for x in contents.split(',')]
		courtNumber = courtNumbers[infoArray[0]]
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
	getLoginInfo('login.txt')