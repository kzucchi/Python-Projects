#create program to detect profanity
#practice code
#what do you love website was removed so this code will not work
#simply practice code to keep writing functions using udacity week 5 python class


#could use post like a pirate to do a different variation of this program
#http://postlikeapirate.com/


import urllib

def read_text():
	quotes = open("/Users/user/Desktop/DonaldTrumpVulgarComments.docx")
	contents_of_file = quotes.read ()
	print (contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
        connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
        output = connection.read()
        print (output)
        connection.close()
        if "true" in output:
                print("Profanity Alert!!")
        elif "false" in output:
                print("This document has no curse words!")
        else:
                print("Could not scan the document properly.")
                
        
read_text()
