
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import pdb
    

# Desired Capabilities
cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "Pixel 6_advent_device",
    "app": "C:\\Users\\Admin\\APk_enable\\app_two_prod_debug_30_05.apk"  # Path to your APK file
}

# Appium server URL
url = 'http://localhost:4723/wd/hub'

# Initialize the WebDriver
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
screenshot_dir = r"C:\Users\Admin\PycharmProjects\pythonProject\screenshots"
# Create the directory if it doesn't exist
if not os.path.exists(screenshot_dir):
     os.makedirs(screenshot_dir)

def take_screenshot(name):
    screenshot_path = os.path.join(screenshot_dir, name)
    driver.save_screenshot(screenshot_path)
    
def click_back1_button(driver):
        retries = 3  # Number of retries
        for _ in range(retries):
         try:
            back_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
            )
            back_button.click()
            return
         except StaleElementReferenceException:
            print("StaleElementReferenceException caught. Retrying...")

   
timeout=90

#My Account 
my_account = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
)
my_account.click()

time.sleep(10) 
take_screenshot("myaccoont.png")

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward(1)'
)


time.sleep(5)
#affilate_program 
affiliate_program = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Affiliate') and contains(@content-desc, 'Program')]"))
 )
affiliate_program.click()
time.sleep(5)
take_screenshot("Affiliate_Program.png")

return_from_affilate = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_affilate.click()
time.sleep(5)

#influencer_registration
influencer_registration = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Influencer') and contains(@content-desc, 'Registration')]"))
)

influencer_registration.click()
time.sleep(5)
take_screenshot("Influencer_Registration.png")
time.sleep(5)
#Return_from_influencer_registration
Return_from_influencer_registration = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
Return_from_influencer_registration.click()
time.sleep(5)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward(2)'
)
# privacy policy
privacy_policy = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]"))
)


privacy_policy.click()
time.sleep(5)
take_screenshot("Privacy_Policy.png")
time.sleep(5)
return_from_privacy_policy = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_privacy_policy.click()
time.sleep(5)
#Terms & condition
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward(2)'
)
terms_and_condn= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Terms') and contains(@content-desc, 'Conditions')]"))
)
terms_and_condn.click()
time.sleep(5)
take_screenshot("terms_condition.png")
time.sleep(5)
return_from_terms_condn = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_terms_condn.click()
time.sleep(5)
#shipping

shipping_button= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Shipping') and contains(@content-desc, 'Button')]"))
)
shipping_button.click()
time.sleep(5)
take_screenshot("shipping.png")
time.sleep(5)
return_from_shipping = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_shipping.click()
time.sleep(5)
#Ticket_by_email

track_by_email= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Track Your Ticket') and contains(@content-desc, 'By Email')]"))
)
track_by_email.click()
time.sleep(5)
take_screenshot("track_by_email.png")
time.sleep(5)
return_track_by_email = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_track_by_email.click()
time.sleep(5)
#about us
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
    'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward(2)'
)
about_us= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'About Us') and contains(@content-desc,'Button')]"))
)
about_us.click()
time.sleep(5)
take_screenshot("about_us.png")
time.sleep(5)
return_about_us = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_about_us.click()
time.sleep(5)
#refer a friend

refer_a_friend= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Refer A Friend') and contains(@content-desc, 'And Earn Discount')]"))
)
refer_a_friend.click()
time.sleep(5)
take_screenshot("refer_friend.png")
time.sleep(5)
return_refer_friend = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_refer_friend.click()
time.sleep(5)
#returns and refunds

return_and_refund= WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Returns') and contains(@content-desc, 'And Refunds')]"))
)
return_and_refund.click()
time.sleep(5)
take_screenshot("return_and_refund.png")
time.sleep(5)
return_and_refund= WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_and_refund.click()
time.sleep(5)

#Cart
cart_icon = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 4"))
)
cart_icon.click()

time.sleep(5)
screenshot_path = os.path.join(screenshot_dir, "Cart.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Designer
Designer_icon = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 1"))
)
Designer_icon.click()

time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "Designer.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#My Store Credit
store_credit_section = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
)
store_credit_section.click()

time.sleep(10)
my_store_credit = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'My Store Credit')]"))
)
my_store_credit.click()
time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "My Store Credit.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from My credit
return_from_mycredit = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_mycredit.click()
time.sleep(10)


#Track Order
track_order = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Track Order')]"))  
)

track_order.click()
time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "Track Order2.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Track Order
return_from_trackorder = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_trackorder.click()
time.sleep(10)



#Choose Language & Currency
choose_language = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Country Currency Button')]"))  
)

choose_language.click()
time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "Language & Currency.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Lang & Currency
return_from_langandcurrency = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_langandcurrency.click()
time.sleep(10)


#Contact US
contact_us= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Contact Us Button')]"))  
)

contact_us.click()
time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "Contact Us2.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Contact Us
return_from_contact_us = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_contact_us.click()
time.sleep(10)

#Secure Shopping
secure_shopping= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Secure Shopping Button')]"))  
)

secure_shopping.click()
time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "Secure Shopping2.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Secure Shopping
return_from_secure_shopping= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_secure_shopping.click()
time.sleep(10)


#Track Your order by guest
track_order_by_guest = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Track Order Guest Button')]"))  
)

track_order_by_guest.click()
time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "guest1.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Track order by guest
return_from_track_order_by_guest= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_track_order_by_guest.click()
time.sleep(10)


#Login inside my account
login= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Login')]"))  
)

login.click()
time.sleep(10)
screenshot_path = os.path.join(screenshot_dir, "Login2.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Track order by guest
element17 = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

element17.click()
time.sleep(10)
menu_icon = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Dashboard Drawer Icon')]"))
)
menu_icon.click()
take_screenshot("menu.png")
time.sleep(2)  # Allow time for the menu to fully open

# pdb.set_trace()
# Women section
women_section = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'Women')]"))
)
women_section.click()

all_women_section = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'All Women')]"))
)
all_women_section.click()
# element12 = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer sub item 1 All Women')]"))
# )
# element12.click()
time.sleep(5)
take_screenshot("women.png")

# Navigate back
back_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
)
back_button.click()
time.sleep(3)

# Men section
men_btn = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'Men') and contains(@content-desc, 'item')]"))
)
men_btn.click()
all_men_section = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'All Men')]"))
)
all_men_section.click()
time.sleep(6)
take_screenshot("men.png")

# Navigate back
time.sleep(5)
click_back1_button(driver)
time.sleep(3)

# Kids section
kids_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'Kids')]"))
)
kids_btn.click()
all_kids_section = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'All Kids')]"))
)
all_kids_section.click()
time.sleep(5)
take_screenshot("kids.png")

# Navigate back
time.sleep(5)
click_back1_button(driver)

