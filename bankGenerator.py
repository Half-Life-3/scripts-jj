import names
from faker import Faker
from random import randint,choice
from random_address import real_random_address
from datetime import datetime



def genBank():#generate testing bank
	pass
	
	
def genBranch(): #generate a testing branch
	branch = dict()
	branch["address"] = real_random_address()["address1"]
	branch["city"] = real_random_address()["city"]
	branch["name"] =  branch["city"] +" Branch"
	branch["state"] = real_random_address()["state"]
	branch["zipcode"] = real_random_address()["postalCode"]
	branch["phone"] = "("+str(randint(201,999))+") "+str(randint(100,999))+"-"+str(randint(1000,9999))
	branch["bankID"] = 1
	branch["id"] = randint(1,100000)
	
	
	return branch
	