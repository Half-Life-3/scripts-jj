import requests


where = "http://localhost:4001/login"

json ={
  "username": "admin123",
  "password": "Admin123!",
}

r = requests.post(where,json=json,headers={"Content-Type": "application/json"})


print(r.status_code)
print(r.headers)

#Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbjEyMyIsImF1dGhvcml0eSI6ImFkbWluaXN0cmF0b3IiLCJpYXQiOjE2NDk0Mzg2NDIsImV4cCI6MTY1MDY0ODI0Mn0.lLkPDRYOwBSPAHLVDEX_FeomQxp67aVaoa-7Qotrim0