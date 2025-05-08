'''
This program:
1. Login to your instagram acct.
2. find influencer's acct and scroll down enough
3. download the images of each posts. 

This is a program download only the thumbnail of the influencer's account.
And this only works in instagram page.
commented out the additional influencers' downloading. enable it as you needed.
This use ChromeDrive.
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Prevents the browser from closing
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/") #this is instagram specific code

username = driver.find_element(By.NAME, "username")
username.send_keys("") #put your username
password = driver.find_element(By.NAME, "password")
password.send_keys("") #put your password
password.send_keys(Keys.RETURN)
time.sleep(5)








############ Hormozi ##################

search = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
search.click()


searchName = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]')
searchName.send_keys("hormozi")
time.sleep(2)
person = driver.find_element(By.CSS_SELECTOR, 'a[href="/hormozi/"]')
person.click()

time.sleep(1)


SCROLL_PAUSE_TIME = 2  # Adjust the pause time as needed
reload_limit = 30  # Number of times to reload (scroll down)
count = 1
download_folder = "imgs/hormozi/" # Make a folder in the img folder 

image_urls = set()

time.sleep(1)

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

reload_count = 0  # Initialize reload count

while reload_count < reload_limit:
    
    images = driver.find_elements(By.CSS_SELECTOR,"._aagv img")

    for image in images:
        #img = container.find_element(By.CSS_SELECTOR,"img")
        imgURL = image.get_attribute("src")
        if imgURL and imgURL not in image_urls:
            image_urls.add(imgURL)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # Stop if no new content is loaded
        break

    last_height = new_height
    reload_count += 1  # Increment reload count

#driver.execute_script("window.scrollTo(0, 0);")

for imgURL in image_urls:
     urllib.request.urlretrieve(imgURL, f"{download_folder}{count}.jpg")
     count+=1









'''
################# Dan Koe ##############################

search = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
search.click()

searchName = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]')
searchName.send_keys("dankoe")
time.sleep(2)
person = driver.find_element(By.CSS_SELECTOR, 'a[href="/thedankoe/"]')
person.click()

time.sleep(1)


SCROLL_PAUSE_TIME = 2  # Adjust the pause time as needed
reload_limit = 30  # Number of times to reload (scroll down)
count = 1
download_folder = "imgs/DanKoe/"

image_urls = set()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

reload_count = 0  # Initialize reload count

while reload_count < reload_limit:
    
    images = driver.find_elements(By.CSS_SELECTOR,"._aagv img")

    for image in images:
        #img = container.find_element(By.CSS_SELECTOR,"img")
        imgURL = image.get_attribute("src")
        if imgURL and imgURL not in image_urls:
            image_urls.add(imgURL)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # Stop if no new content is loaded
        break

    last_height = new_height
    reload_count += 1  # Increment reload count

#driver.execute_script("window.scrollTo(0, 0);")

for imgURL in image_urls:
     urllib.request.urlretrieve(imgURL, f"{download_folder}{count}.jpg")
     count+=1












############# Matt Gray ##############

search = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
search.click()

searchName = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]')
searchName.send_keys("mattgray")
time.sleep(2)
person = driver.find_element(By.CSS_SELECTOR, 'a[href="/matthgray/"]')
person.click()

time.sleep(1)


SCROLL_PAUSE_TIME = 2  # Adjust the pause time as needed
reload_limit = 30  # Number of times to reload (scroll down)
count = 1
download_folder = "imgs/Mattgray/"

image_urls = set()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

reload_count = 0  # Initialize reload count

while reload_count < reload_limit:
    
    images = driver.find_elements(By.CSS_SELECTOR,"._aagv img")

    for image in images:
        #img = container.find_element(By.CSS_SELECTOR,"img")
        imgURL = image.get_attribute("src")
        if imgURL and imgURL not in image_urls:
            image_urls.add(imgURL)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # Stop if no new content is loaded
        break

    last_height = new_height
    reload_count += 1  # Increment reload count

#driver.execute_script("window.scrollTo(0, 0);")

for imgURL in image_urls:
     urllib.request.urlretrieve(imgURL, f"{download_folder}{count}.jpg")
     count+=1










########### Codie Sachez ####################

search = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
search.click()

searchName = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]')
searchName.send_keys("codiesanchez")
time.sleep(2)
person = driver.find_element(By.CSS_SELECTOR, 'a[href="/codiesanchez/"]')
person.click()

time.sleep(1)


SCROLL_PAUSE_TIME = 2  # Adjust the pause time as needed
reload_limit = 30  # Number of times to reload (scroll down)
count = 1
download_folder = "imgs/CodieSanchez/"

image_urls = set()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

reload_count = 0  # Initialize reload count

while reload_count < reload_limit:
    
    images = driver.find_elements(By.CSS_SELECTOR,"._aagv img")

    for image in images:
        #img = container.find_element(By.CSS_SELECTOR,"img")
        imgURL = image.get_attribute("src")
        if imgURL and imgURL not in image_urls:
            image_urls.add(imgURL)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # Stop if no new content is loaded
        break

    last_height = new_height
    reload_count += 1  # Increment reload count

#driver.execute_script("window.scrollTo(0, 0);")

for imgURL in image_urls:
     urllib.request.urlretrieve(imgURL, f"{download_folder}{count}.jpg")
     count+=1












######### Simon Hoiberg ################

search = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
search.click()

searchName = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]')
searchName.send_keys("simonhoiberg")
time.sleep(2)
person = driver.find_element(By.CSS_SELECTOR, 'a[href="/simonhoiberg/"]')
person.click()

time.sleep(1)


SCROLL_PAUSE_TIME = 2  # Adjust the pause time as needed
reload_limit = 30  # Number of times to reload (scroll down)
count = 1
download_folder = "imgs/SimonHoiberg/"

image_urls = set()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

reload_count = 0  # Initialize reload count

while reload_count < reload_limit:
    
    images = driver.find_elements(By.CSS_SELECTOR,"._aagv img")

    for image in images:
        #img = container.find_element(By.CSS_SELECTOR,"img")
        imgURL = image.get_attribute("src")
        if imgURL and imgURL not in image_urls:
            image_urls.add(imgURL)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # Stop if no new content is loaded
        break

    last_height = new_height
    reload_count += 1  # Increment reload count

#driver.execute_script("window.scrollTo(0, 0);")

for imgURL in image_urls:
     urllib.request.urlretrieve(imgURL, f"{download_folder}{count}.jpg")
     count+=1








############### Greg Isenberg ##################

search = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search"]')
search.click()

searchName = driver.find_element(By.CSS_SELECTOR, '[aria-label="Search input"]')
searchName.send_keys("gregisenberg")
time.sleep(2)
person = driver.find_element(By.CSS_SELECTOR, 'a[href="/gregisenberg/"]')
person.click()

time.sleep(1)


SCROLL_PAUSE_TIME = 2  # Adjust the pause time as needed
reload_limit = 30  # Number of times to reload (scroll down)
count = 1
download_folder = "imgs/GregIsenberg/"

image_urls = set()

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

reload_count = 0  # Initialize reload count

while reload_count < reload_limit:
    
    images = driver.find_elements(By.CSS_SELECTOR,"._aagv img")

    for image in images:
        #img = container.find_element(By.CSS_SELECTOR,"img")
        imgURL = image.get_attribute("src")
        if imgURL and imgURL not in image_urls:
            image_urls.add(imgURL)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # Stop if no new content is loaded
        break

    last_height = new_height
    reload_count += 1  # Increment reload count

#driver.execute_script("window.scrollTo(0, 0);")

for imgURL in image_urls:
     urllib.request.urlretrieve(imgURL, f"{download_folder}{count}.jpg")
     count+=1


'''

driver.close()
