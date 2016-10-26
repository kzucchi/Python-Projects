#create program to detect profanity

def read_text():
	quotes = open("/Users/user/Desktop/DonaldTrumpVulgarComments.docx")
	contents_of_file = quotes.read ()
	print (contents_of_file)
	quotes.close()
read_text()
