from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from pathlib import Path


opts = Options()
#opts.add_argument("--headless")
opts.binary_location=r'C:\Program Files\WindowsApps\Mozilla.Firefox_113.0.2.0_x64__n80bbvh6b1yt2\VFS\ProgramFiles\Firefox Package Root\firefox.exe'
profile = FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)  # Use a custom folder for downloads

# NOT WORKING
#profile.set_preference("browser.download.dir", '/app')  # Set the custom download folder path

# WORKING AS IT MUST BE AN ABSOLUTE PATH
#profile.set_preference("browser.download.dir", r'D:\m01.repos\github.1\py.se.firefox.setDownloadsPath') # use the fullpath

# SOLUTION TO USE RELATIVE PATH TO CURRENT PYTHON SCRIPT
myPath = Path('./app').absolute()
pathToFolder=myPath._str
profile.set_preference("browser.download.dir", pathToFolder) # use the fullpath

profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # Disable the download dialog
driver = webdriver.Firefox(firefox_profile=profile, executable_path='./geckodriver', options=opts)
driver.get(r'https://freemidi.org/download3-27909-mongolia-old-national-anthems')
print('wait please')