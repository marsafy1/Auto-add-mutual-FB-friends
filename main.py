# selenium setup
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Coloring lib
import colorama
from colorama import Fore

# For reading the JSON file
import json

# Time lib
import time

nme = 'mohamedkhallid72@gmail.com'
passwrd = 'mmrrss909909'

min_mutual_friends_count = 1

successColor = Fore.GREEN 
dangerColor = Fore.RED
infoColor = Fore.WHITE
actionColor = Fore.BLUE

def getConfigs():
    try:
        f = open('configs.json')
        data = json.load(f)
        nme = data['email']
        passwrd = data['password']
        min_mutual_friends_count = data['min_mutual_friends']
        print(successColor + "Read the config file Successfully")

        f.close()
    except:
        print(dangerColor + "Couldnt read the config file")
        exit()




def safityDelay():
    time.delay(1)

def run():  

    getConfigs()

    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/friends")	# go to facebook.com

    login(driver)
    seeAllFriends(driver)

def handleFriendRequest(friend, mutualFriendsCount, index):
    if(int(mutualFriendsCount) >= min_mutual_friends_count):
        try:
            confirms = friend.find_elements(By.XPATH,"//span[text()='Confirm']")
            confirms[index].click()
            print(actionColor + "added this friend")
        except:
            print(dangerColor + "Couldnt add this friend")

def findMutualFriends(friend):
    for elem in friend.find_elements(By.CLASS_NAME,"xuxw1ft"):
        if('mutual friend' in elem.get_attribute("innerHTML")):
            return (elem.get_attribute("innerHTML").split(" "))[0]
    return -1

def handleFriend(friend, count):
        try:
            name = friend.find_element(By.CLASS_NAME,"xuxw1ft").get_attribute("innerHTML")
            mutualFriendsCount = findMutualFriends(friend)

            if(mutualFriendsCount != -1):
                print(infoColor + str(count) + " " +name +" with " + str(mutualFriendsCount) + " mutual friend(s)")
                handleFriendRequest(friend, mutualFriendsCount, count - 1)
            else:
                print(infoColor + str(count) + " " +name +" with " + str(0) +" mutual friend(s)")
            
        except:
            pass

def seeAllFriends(driver):
    friendsContainer = driver.find_element(By.CLASS_NAME, "x8gbvx8")
    allFriends = friendsContainer.find_elements(By.XPATH, "*")

    count = 1
    for friend in allFriends:
        handleFriend(friend, count)
        count += 1

    
def getElem(source, by, q):
    try:
        source.find_element(by, q)
    except:
        print(dangerColor + "Couldnt find the element.")
def login(driver):
    try:
        if driver:
            email = driver.find_element(By.NAME, "email")
            email.send_keys(nme)
            email.send_keys(Keys.TAB)

            password = driver.find_element(By.NAME,"pass")	# search password textbox
            password.send_keys(passwrd)	


            loginBtn = driver.find_element(By.NAME, "login")
            loginBtn.click()
            print(successColor + "Logged In Successfully")

        else:
            print(dangerColor + "Driver does not exist")
            
    except:
        print(dangerColor + "Couldnt login")

run()