import requests


where = "http://localhost:8080/users/registration"

json ={
  "username": "member123",
  "password": "Member123!",
  "role": "member",
  "firstName": "larry",
  "lastName": "dudebro",
  "email": "adminnn@admin.com",
  "phone": "(123) 456-8710"
}

r = requests.post(where,json=json,headers={"Content-Type": "application/json"})


print(r.status_code)
print(r.headers)