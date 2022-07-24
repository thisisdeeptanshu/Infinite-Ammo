from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as pog

websites = ["https://parade.com/973277/jessicasager/inspirational-quotes/"]
totalWebsites = 1
max_websites = 25
quotes = []

i = 0
while True:
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(websites[i])

    for p in driver.find_elements(By.TAG_NAME, "p"):
        try:
            if int(p.text.split(". ")[0]):
                if p.text.split(". ")[1] not in quotes:
                    quotes.append(p.text.split(". ")[1])
                try:
                    a = p.find_element(By.TAG_NAME, "a")
                    if a.get_attribute("href") not in websites and "quote" in a.get_attribute("href") and totalWebsites < max_websites:
                        websites.append(a.get_attribute("href"))
                        totalWebsites += 1
                except:
                    pass
        except:
            pass
    driver.close()
    i += 1
    if i  == totalWebsites:
        break

with open("quotes.txt", "w") as f:
    f.writelines(quotes)