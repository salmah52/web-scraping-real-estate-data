import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


with open("Main2_estate.csv", "w", encoding="utf-8") as file:
    file.write("Room, Location, Description, Duration, Price, Bedroom, Bathroom, Toilet, Parking, Contact \n")
    
#initialize Firefox
#driver=webdriver.Firefox(executable_path='C:/bin/geckodriver.exe')

#initialize Chrome
driver =webdriver.Chrome(executable_path= r"C:\Users\lasis\OneDrive\Desktop\webdrivers\chromedriver.exe")


#Open URL

rent = "https://nigeriapropertycentre.com/"

driver.get(rent)
driver.maximize_window()


#serach by rent
rent = driver.find_element(By.XPATH,'//*[@id="li-cid-for-rent"]/a/label')
rent.click()

#search by type
type =  driver.find_element(By.XPATH,'//*[@id="tid"]/option[2]')
type.click()
time.sleep(1)

#seacr by bedroom
bedroom =  driver.find_element(By.XPATH,'//*[@id="bedrooms"]')
bedroom.click()
time.sleep(1)

#seacr by minprice
minprice =  driver.find_element(By.XPATH,'//*[@id="minprice"]')
minprice.click()
time.sleep(1)

#seacr by maxprice
maxprice =  driver.find_element(By.XPATH,'//*[@id="maxprice"]')
maxprice.click()
time.sleep(1)

#seacr by search
search =  driver.find_element(By.XPATH,'//*[@id="search_jsForm"]/div[4]/div/div/div/div/div/div[2]/div/div[4]/button/span')
search.click()
time.sleep(1)

#seacr by Lagos
Lagos =  driver.find_element(By.XPATH,'//*[@id="rmjs-1"]/li[25]/a')
Lagos.click()
time.sleep(1)

for k in range(1, 700, 1):
    Rooms = driver.find_elements(By.XPATH, '//a/h4[@class="content-title"]')
    Locations = driver.find_elements(By.XPATH, '//div[3]/address/strong')
    Descriptions = driver.find_elements(By.XPATH, '//div[@class="description hidden-xs"]/p')
    Durations = driver.find_elements(By.XPATH, '//span[@class="added-on added-recently"] ')
    Prices = driver.find_elements(By.XPATH, "//span[1]/span[2]")
    Bedrooms = driver.find_elements(By.XPATH, "//div/div/div[4]/ul/li[1]/span[1]") 
    Bathrooms = driver.find_elements(By.XPATH, "//div/div/div[4]/ul/li[2]/span[1]")
    Toilets = driver.find_elements(By.XPATH, "//div/div/div[4]/ul/li[3]/span[1]")
    Parkings = driver.find_elements(By.XPATH, "//div/div/div[4]/ul/li[4]/span[1]")
    Contacts = driver.find_elements(By.XPATH, "//div/div/div[3]/div[3]/span[3]")

    with open("Main2_estate.csv", "a", encoding="utf-8") as file:
        for i in range(len(Rooms)):
            file.write(Rooms[i].text.replace(',', '') + "," + Locations[i].text.replace(',', '') + ","  
                   + Descriptions[i].text.replace(',', '') + "," + (Durations[i].text.replace(',', '') if len(Durations) > i else "") + "," 
                   + Prices[i].text.replace(',', '').replace(',', '') + "," 
                   + (Bedrooms[i].text.replace(',', '').replace(',', '') if len(Bedrooms) > i else "") + ","
                   + (Bathrooms[i].text.replace(',', '').replace(',', '') if len(Bathrooms) > i else "") + ","
                   + (Toilets[i].text.replace(',', '').replace(',', '') if len(Toilets) > i else "") + ","
                   + (Parkings[i].text.replace(',', '').replace(',', '') if len(Parkings) > i else "") + ","
                   + (Contacts[i].text.replace('\n', '-').replace('\n', '-') if len(Contacts) > i else "") + ","
                      # print(text.replace('\n', ' - '))
                    "\n")
    
    # Add a small delay to allow the page to load
    time.sleep(3)
    
    current_url = driver.current_url
    print(f"Scraping page {k}: {current_url}")
    
    driver.find_element(By.LINK_TEXT,'›')
    
    next_buttons = driver.find_elements(By.LINK_TEXT,'›')
    print(f"Number of next buttons found: {len(next_buttons)}")
    
    if len(next_buttons) > 0:
        next_button = next_buttons[0]
        next_button.click()
    else:
        break
    
#close the driver
driver.close()


#Extra

# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import StaleElementReferenceException

# try:
#     Contacts = driver.find_elements(By.XPATH, "//div/div/div[3]/div[3]/span[3]")
#     for contact in Contacts:
#         text = contact.text
#         print(text.replace('\n', ' - '))
# except StaleElementReferenceException:
#     # If StaleElementReferenceException is raised, locate the element again
#     Contacts = driver.find_elements(By.XPATH, "//div/div/div[3]/div[3]/span[3]")
#     for contact in Contacts:
#         text = contact.text
#         print(text.replace('\n', ' - '))


# print("Rooms length:", len(Rooms))
# print("Locations length:", len(Locations))
# print("Descriptions length:", len(Descriptions))
# print("Durations length:", len(Durations))
# print("Prices length:", len(Prices))
# print("Bedrooms length:", len(Bedrooms))
# print("Bathrooms length:", len(Bathrooms))
# print("Toilets length:", len(Toilets))
# print("Parkings length:", len(Parkings))
# print("Contacts length:", len(Contacts))
