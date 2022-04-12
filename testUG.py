import userGenerator as ug
import sendApps as app
import unittest

#print(ug.genUsers(None))

class TestUserGeneration(unittest.TestCase):
	
	def test_createAUser(self): #whether a generated user name is 2 strings
		aName = ug.genUsers(1)[0]
		self.assertEqual(type(aName[0]),str)
		self.assertEqual(type(aName[1]),str)
		
		
		
class TestAppGeneration(unittest.TestCase):
	def test_sendAnApp(self): #whether a generated app results in a sucess state
		self.assertEqual(app.sendApp()[0],201)
		
		
		
if __name__=="__main__":
	unittest.main()