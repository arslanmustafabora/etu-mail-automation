from selenium import webdriver

URL = "https://webmail.etu.edu.tr/roundcube/?_task=mail&_mbox=INBOX"

ID = input("Enter your ID:")
PASS = input("Enter your password: ")

br = webdriver.Chrome()
br.get(URL)

userID = br.find_element_by_xpath("//*[@id='rcmloginuser']")
password = br.find_element_by_xpath("//*[@id='rcmloginpwd']")
button = br.find_element_by_xpath("//*[@id='rcmloginsubmit']")


userID.send_keys(ID)
password.send_keys(PASS)
button.click()
br.maximize_window()


subjects = br.find_elements_by_class_name("message")

for subject in subjects:
    print(subject.text)

br.quit()
