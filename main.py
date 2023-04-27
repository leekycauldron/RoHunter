from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import json

#read settings.json
with open("settings.json", "r") as f:
    settings = json.load(f)

#set variables from settings.json
target_name = settings["user"]
profile_link = settings["profile-link"]
data_dir = settings["chrome"]["data-dir"]
chrome_profile = settings["chrome"]["profile"]
links = settings["links"]
delay = settings["delay"]

#set chrome options and start service
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={data_dir}")
options.add_argument(f'--profile-directory={chrome_profile}')
ser = Service("chromedriver.exe")



# main loop

driver = webdriver.Chrome(service=ser, options=options)
try:
    # Check if online before searching links
    

    while True:
            driver.get(profile_link)
            try:
                x = driver.find_element(By.CLASS_NAME,"profile-header-top")
                try:
                    y = driver.find_element(By.CLASS_NAME,"game")
                    if "chat-friend-status" in y.get_attribute("class"):
                        print("Offline")
                        time.sleep(delay)
                        continue
                    print("Online")
                    
                    break
                except:
                    print("Offline")
                    time.sleep(delay)
                    continue
            except Exception as e:
                print(e)
                pass

    # Search links after checking if online 
    found = False
    while not found:

        for link in links:
            print(link)
            driver.get(link+"#!/game-instances")
            while True:
                try:
                    search_bar = driver.find_element("id","sbx-input")
                    break
                except:
                    pass
            search_bar.send_keys(target_name)
            search_btn = driver.find_element("id","sbx-search")
            search_btn.click()
            
            # Wait for search to start loading
            time.sleep(1)
            while True:
                stat = driver.find_element("id","sbx-status")
                if stat.text != "Searching...":
                    break
            print(stat.text)
            # End search if target is found
            if stat.text == "Found target":
                print(f"Found {target_name} in {link}!")
                driver.close()
                found = True
                break
            time.sleep(delay)


except KeyboardInterrupt:
    driver.close()