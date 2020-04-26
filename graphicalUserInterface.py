import pyautogui

def login():

	userName = pyautogui.prompt(text = "Enter your username", title = "USERNAME", default = "")
	password = pyautogui.password(text = "Enter your password", title = "PASSWORD", default = "")
	return userName, password


def screen(subjects):

	empty = ""
	for i in range(20):

		empty += str(subjects[i].text)+"\n"

	pyautogui.alert(text= empty, title = "Recently", button = "Okey")
   	
