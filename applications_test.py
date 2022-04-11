import faker
import requests
import datetime
from random_address import real_random_address
import random

def create_date()
	f = Faker()
	start = datetime.date(year=1900,month=1,day=1)
	age=18
	end = datetime.date(year=2022 - age,month=1,day=1)
	return fale.date_between(start_date=start,end_date=end)
	
	
def application()







def apply(auth):
	where =""
	json = create_app()
	head = {"Content-Type":"application/json","Authorization":auth}
	r = requests.post(where,json=json,headers=head)
	print(r.status_code)
	print(r.headers)
	
	
	
	
#Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbjEyMyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NDk0Mzg2NDIsImV4cCI6MTY1MDY0ODI0Mn0.lLkPDRYOwBSPAHLVDEX_FeomQxp67aVaoa-7Qotrim0

apply("Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbjEyMyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NDk0Mzg2NDIsImV4cCI6MTY1MDY0ODI0Mn0.lLkPDRYOwBSPAHLVDEX_FeomQxp67aVaoa-7Qotrim0")
