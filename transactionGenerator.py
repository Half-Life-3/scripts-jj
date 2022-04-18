import names
from faker import Faker
from random import randint, choice
from random_address import real_random_address
from datetime import datetime


def genTrans(account,card): #generate a testing transaction
	trans = dict()
	trans["type"] = choice([ "DEPOSIT", "WITHDRAWAL", "TRANSFER_IN", "TRANSFER_OUT", "PURCHASE", "PAYMENT", "REFUND", "VOID" ])
	trans["method"] = choice([ "ACH", "ATM", "CREDIT_CARD", "DEBIT_CARD", "APP" ])
	trans["amount"] = 5
	trans["merchantCode"] = "ALINE"
	trans["merchantName"] = "Aline Financial"
	trans["accountNumber"] = account
	trans["cardNumber"] = card
	trans["hold"] = True
	
	return trans
	