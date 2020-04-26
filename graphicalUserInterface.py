import pyautogui

def screen(subjects):

	empty = ""
	for i in range(10):

		empty += str(subjects[i].text)+"\n"

	pyautogui.alert(text= empty, title = "Recently", button = "Okey")
   	
