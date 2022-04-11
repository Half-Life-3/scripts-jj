import names
from faker import Faker
from random import randint,choice
from random_address import real_random_address
from datetime import datetime


def genUsers(num): #take a number, return that many names as a list of [firstName,lastName]
	if num is None:
		try:
			num = int(input("How many Users to generate? ")) #prompt for a number of users to generate if a none argument is passed
		except Exception as e:
			num = 10 #give a defult if there's an error
	namesList=[]
	for i in range(num):
		name=[]
		
		name.append(names.get_first_name())
		name.append(names.get_last_name())
		namesList.append(name) #append names to list in form [firstName,lastName]
		#print(names.get_full_name())
	return namesList
		
		
def genDOB(minAge = 18): #make a random birthday
	yr = randint(1900, datetime.now().year-(minAge+1)) #ensure the birthyear assures user is at least minAge years old (accounting for months)
	mo = randint(1,12)
	day = randint (1,28)
	dateStr = str(yr)+"-"+"{:0>2}".format(mo)+"-"+"{:0>2}".format(day) #format string to look like a date, prepending a 0 to single-didgit items if needed 
	dateSet = (yr,mo,day)
	return (dateStr,dateSet) #return a str for inputs, and a set for quick indexing or debugging
#print(namesList)



# {
# firstName*	string
# middleName	string
# lastName*	string
# dateOfBirth*	string($date)
# gender*	string
# Enum:
# Array [ 4 ]
# email*	string
# phone*	string
# socialSecurity*	string
# driversLicense*	string
# income*	integer($int32)
# minimum: 0
# address*	string
# city*	string
# state*	string
# zipcode*	string
# mailingAddress*	string
# mailingCity*	string
# mailingState*	string
# mailingZipcode*	string
# }

def genCredentials(name): #take a name as [firstName,lastName] and return a dict of credentials for that name

	if len(name)<2:
		name = ["FNU","LNU"]
	elif type(name) ==str:
		name = [name,"LNU"] #todo:case the input name is form "firstname lastname"
		
		
	user =dict()
	dob = genDOB()
	user["firstName"]= name[0]
	user["lastName"] = name[1]
	user["dateOfBirth"] = dob[0]
	user["gender"] = choice(["MALE","FEMALE","OTHER","UNSPECIFIED"])
	user["email"] = name[0].lower()+"."+name[1].lower()+"@email.com"
	user["phone"] = "("+str(randint(201,99))+") "+str(randint(100,999))+"-"+str(randint(1000,9999))
	user["username"] = "ALINEBANK_TEST_"+name[0].lower()[0] +name[1].lower() + str(dob[1][0]) # "John Doe born in 2005 becomes 'ALINEBANK_TEST_Jdoe2005'
	
	
	
	