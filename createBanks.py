import bankGenerator as bg 
import requests




def createBank():
	where = "http://localhost:8083/branches"
	json= bg.genBank()
	
	r=requests.post(where,json=json,headers={"Content-Type":"application/json","Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbjEyMyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NDk0Mzg2NDIsImV4cCI6MTY1MDY0ODI0Mn0.lLkPDRYOwBSPAHLVDEX_FeomQxp67aVaoa-7Qotrim0"})
	
	return (r.status_code,r.text)


def createBranch():
	where = "http://localhost:8083/branches"
	json = bg.genBranch()
	
	r=requests.post(where,json=json,headers={"Content-Type":"application/json","Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbjEyMyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NDk0Mzg2NDIsImV4cCI6MTY1MDY0ODI0Mn0.lLkPDRYOwBSPAHLVDEX_FeomQxp67aVaoa-7Qotrim0"})
	
	return (r.status_code,r.text)
	
	
	
