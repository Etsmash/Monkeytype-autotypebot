


try:
    import pip
except:
    print("pip is not installed. Install pip before accessing this program")
    sys.exit()

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
    from pynput.keyboard import Key, Controller
except:
    install('pynput')
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
except:
    install('selenium')
    install('webdriver_manager')
try:
    import time
except:
    install('time')
try:
    import os
except:
    install('os')
try:
    import sys
except:
    install('sys')
try:
    import random
    from random import randint, randrange
except:
    install('random')
keyboard = Controller()
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://monkeytype.com')
play = 0
while play == 0:
    asking = input("ready?").lower()
    if asking == "yes":
         play = 1

    elif asking == "no":
        print("ok")   

    else:
        print("Input yes or no")

play = 0 
while play == 0:
    amountofword = str(input("Do you want your words to be written like a human, or a bot?")).lower()
    if amountofword == "human":
        play = 1
        repeat = random.uniform(0.2, 0.6)
    elif amountofword == "bot":
        words = str(input("Delay between each word?"))

        try:
            repeat = float(words)
            play = 1
        except:
            print("Use floating number only")
        
    else:
        print("""Respond with:
        1. bot
        2. human
        """)
again = 0
while again == 0:
    words = driver.find_elements_by_xpath('//div[@class="word"]')
    activewords = driver.find_elements_by_xpath('//div[@class="word active"]')
    activeword = []
    for p in range(len(activewords)):
        activeword.append(activewords[p].text)
    Wordlist = [""]
    print(Wordlist)
    print("get on the page and click to go in view")
    time.sleep(10)
    io = 0
    Valid = 0
    wordwritten = 0
    print(activeword)
    fortnite = str(activeword[0])
    keyboard.type(fortnite)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    wordsburst = 0
    while Valid == 0:
        if Wordlist[io] == "":
            if amountofword == "human":
                repeat = random.uniform(0.2, 1.0)
            #The time.sleep is the delay between each word written.
            time.sleep(repeat)
            active = []
            actword = driver.find_elements_by_xpath('//div[@class="word active"]')
            for p in range(len(actword)):
                active.append(actword[p].text)
            print(active)
            o = len(str(active)) - 2 
            oof = str(active)[2:o]
            try:
                if active[0] == "":
                    sys.exit()
            except:
                sys.exit()
            keyboard.type(oof)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            wordsburst = 0
        
        else:
            io = io + 1
            wordwritten = wordwritten + 1
            wordsburst = wordsburst + 1
    
        if wordwritten == 200:
            Valid = 1