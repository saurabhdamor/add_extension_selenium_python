# First, import 'WebDriver' from 'SELENIUM' Library
from selenium import webdriver


# Copy your 'GECKODRIVER.EXE' path link & paste in between '  '
driver = webdriver.Firefox(executable_path=r'C:\Users\saurabh\Documents\gecodriver\geckodriver.exe')


# Paste your web-site URL-LINK in between '  '
driver.get('https://www.google.com/recaptcha/api2/demo')


# Paste your 'EXTENSION(.XPI)' file, folder path in between '  '
extension_dir = 'C:\\Users\\saurabh\\Downloads\\yoyo\\'


# Go to your 'EXTENSION(.XPI)' file & copy that file name with .xpi format
extensions = ['buster_captcha_solver_for_humans-1.2.0-an+fx.xpi']


# Here, we install 'EXTENSION(.XPI)' in Firefox browser
for extension in extensions:
    driver.install_addon(extension_dir + extension, temporary=True)


# Wait for 10 sec
driver.implicitly_wait(10)


# Close browser 'TAB'
driver.close()