import transactionGenerator as tg
import requests



def createTransaction(account,card):
	where = "http://localhost:8073/transactions"
	json = tg.genTrans(account,card)
	
	r=requests.post(where,json=json,headers={"Content-Type":"application/json","Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbjEyMyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NDk0Mzg2NDIsImV4cCI6MTY1MDY0ODI0Mn0.lLkPDRYOwBSPAHLVDEX_FeomQxp67aVaoa-7Qotrim0"})
	
	return (r.status_code,r.text)