import userGenerator as ug
import requests



def sendApp():
	where = "http://localhost:8071/applications"
	name = ug.genUsers(1)
	json = ug.genApp(name[0])
	
	r=requests.post(where,json=json,headers={"Content-Type":"application/json"})
	
	return (r.status_code,r.text)

def sendApps(num,debug=False):
	where = "http://localhost:8071/applications"
	name = ug.getUsers(num)
	output=[]
	for i in range(num):
		json=ug.genApp(name[i])
		r.requests.post(where,json=json,headers={"Content-Type":"application/json"})
		output.append((r.status_code,r.text))
		if debug:
			print(r.status_code)
	return output



# def sendTestApp(num):
	# where = "http://localhost:8071/applications"
	# names = ug.genUsers(num)

	# json = ug.genApp(names[0])

# r=requests.post(where,json=json,headers={"Content-Type":"application/json"})

# print(r.status_code)
# print(r.headers)
# print(r.text)

