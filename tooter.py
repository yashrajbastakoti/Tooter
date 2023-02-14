toots = open("toots.csv",'r') # opens toots file to read
users = open("users.csv",'r') #opens user file to read
toots2 = open("toots.csv",'a') #opens toots file to append
from datetime import datetime
class Tooterr:
	def __init__(self):
			self.pin = ""
			self.name = ""
			self.handle = ""
			self.following = ""
			self.d = {}

	def enterPin(self): #asks pin from the user
			pin = input("Please enter your pin here: ")
			if pin =="":
				print("Your pin cannot be nothing")
				self.enterPin() 
			else:
				self.setPin(pin)
				return pin
				
	def setPin(self, pin): #sets the pin of the user
		self.pin = pin
		
	def enterHandle(self): #asks for handle
			handle = input("Please enter your handle here: ")
			if handle =="":
				print("Your handle cannot be nothing")
				self.enterHandle()
			else:
				self.setHandle(handle)
				return handle
				
	def setHandle(self, handle): #sets the handle of the user
		self.handle = handle
		
	def getName(self):
		name = self.d[self.handle][1]
		return(name)
		
	def makeDictionary(self): #makes a dictionary of user file with key being the handle and value being everything else
		for list1 in users:
			userList = list1.split(",")
			self.d[userList[0]] = userList
		return(self.d)
		
	def checkHandlePin(self): #checks if the handle and pin exixts in user file
			self.makeDictionary()
			found = False
			for keys in self.d:
				if keys == self.handle:
					if self.pin in self.d[self.handle]:
						found = True
						break
			if found == True: #if the handle and pin exixts runs self.readwrite function
				print("""HELLO """ + str(self.getName()))
				print("""What do you want to do today?""")
				self.readwrite()
			else:
				print("We couldn't find your account! Please try again.")
				
	def getOptionFromUser(self):
			"""Takes a list of strings, prints them, prompts user for a selection,
			and returns the index of the selected option. returns -1 if failed/exiting."""

			for idx in range(len(optionList)):
				print("Press " + str(idx+1) + " if you want to " + optionList[idx])

			while True:
				try:
					selection = input("Enter your selection: ")
					exitCodes = ["exit", "q", "quit"]
					if selection in exitCodes: # user typed in exit code
						return -1

					option = int(selection)
					if option < 1 or option > len(optionList):
						print("Invalid selection. Please try again.")
						continue
				except ValueError:
					print("Invalid input. Please enter a number.")
					continue
				except EOFError: # ctrl-d
					return -1
				except KeyboardInterrupt: # ctrl-c
					print() # adds newline to clean up output
					return -1

				# return option
				return option 
	
	def readwrite(self): #redirects to either seeFeed or writeTweet accorfing to the input in option
		option = self.getOptionFromUser()
		if option == 1:
			print(""" Here is your feed """)
			self.seeFeed()
		elif option == 2:
			print(""" Lets TOOT """)
			self.writeTweet()
	
	def seeFeed(self): # co
		self.makeDictionary()
		a = self.d[self.handle][3]
		following = a.split("-")
		following[-1] = following[-1][0:-1] #removing the \n from the 3rd value
		List=[""]
		for Line in toots:
			List =Line.split(",")
			for people in following:
				if people == List[0]:
					print("At " + List[1] + " " + List[0] + " tweeted: " + List[2]) #printing the tweet of the following in a format
		
	def writeTweet(self): #gets tweet from the user and saves it to the toots2 file
		newTweet = input("Write your toot here:")
		today = datetime.today().strftime('%m/%d/%Y') #gets todays date and time
		inputt = self.handle+","+today+","+newTweet
		toots2.write("\n"+inputt)
		print("""Tooted!! See You Again.""")
				
optionList = ["see your feed.", "write a tweet."]
			
def main():
	print(""" WELCOME TO TOOTER """)
	tooter = Tooterr()
	tooter.enterHandle()
	tooter.enterPin()
	tooter.checkHandlePin()


main()
toots2.close()
toots.close()
users.close()
			
