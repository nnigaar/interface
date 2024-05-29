import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.wikipedia.org/")

wait = WebDriverWait(driver, 10)

# Locate the elements
eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.central-textlogo')))
width = eleCookiesDiv.size['width']
color = eleCookiesDiv.value_of_css_property("color")
print(width == 270)  # Width değerini piksel cinsinden kontrol ediyoruz
print(color == "rgba(0, 0, 0, 1)")


eleCookiesDiv1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.central-featured-logo')))
width = eleCookiesDiv1.size['width']
height = eleCookiesDiv1.size['height']
print(width == 200)  # Width değerini piksel cinsinden kontrol ediyoruz
print(height == 183)  # Height değerini piksel cinsinden kontrol ediyoruz


eleCookiesDiv2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'strong.jsl10n.localized-slogan')))
color = eleCookiesDiv2.value_of_css_property("color")
width = eleCookiesDiv2.size['width']
print(width == 176)  # Width değerini piksel cinsinden kontrol ediyoruz
print(color == "rgba(0, 0, 0, 1)")


eleCookiesDiv3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.pure-button-primary-progressive')))
background_color = eleCookiesDiv3.value_of_css_property("background-color")
print(background_color == "rgba(51, 102, 204, 1)")  # Arka plan rengini doğruluyoruz

eleCookiesDiv4 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'i.sprite.svg-search-icon')))
width = eleCookiesDiv4.size['width']
height = eleCookiesDiv4.size['height']
color = eleCookiesDiv4.value_of_css_property("color")
print(color == "rgba(255, 255, 255, 1)")  # Arka plan rengini doğruluyoruz
print(width == 22)  # Width değerini piksel cinsinden kontrol ediyoruz
print(height == 22)  # Height değerini piksel cinsinden kontrol ediyoruz


eleCookiesDiv5 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'i.sprite.svg-language-icon')))
width = eleCookiesDiv5.size['width']
height = eleCookiesDiv5.size['height']
print(width == 22)  # Width değerini piksel cinsinden kontrol ediyoruz
print(height == 22)  # Height değerini piksel cinsinden kontrol ediyoruz

eleCookiesDiv6 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.footer-sidebar-icon.sprite.svg-Wikimedia-logo_black')))
color = eleCookiesDiv6.value_of_css_property("color")
width = eleCookiesDiv6.size['width']
height = eleCookiesDiv6.size['height']
print(width == 42)  # Width değerini piksel cinsinden kontrol ediyoruz
print(height == 42)  # Height değerini piksel cinsinden kontrol ediyoruz
print(color == "rgba(0, 0, 0, 1)")

eleCookiesDiv7 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#searchInput')))
height = eleCookiesDiv7.size['height']
print(height == 44)  # Height değerini piksel cinsinden kontrol ediyoruz

eleCookiesDiv6 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav.central-featured')))
width = eleCookiesDiv6.size['width']
height = eleCookiesDiv6.size['height']
print(width == 546)  # Width değerini piksel cinsinden kontrol ediyoruz
print(height == 325)  # Height değerini piksel cinsinden kontrol ediyoruz

