
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
    "deviceName": "Galaxy_Nexus_API_34",
    "app": "C:\\Users\\Admin\\APk_enable\\app_two_prod_debug_30_05.apk"  # Path to your APK file
}

# Appium server URL
url = 'http://localhost:4723/wd/hub'

# Initialize the WebDriver
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
screenshot_dir = r"C:\Users\Admin\PycharmProjects\Appium_Automation\screenshots"
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

 
def test_scroll(button_xpath):
    time.sleep(3)
    i=0
    for i in range(20):
        try:
            print(f"Attempt {i+1}: Trying to find 'Contact Us Button'")
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, button_xpath))
            )
        
                 
            print("Element found, clicking 'Contact Us Button'")
            element.click()
            test_back_button = WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
            break  # Exit loop after successful click
        
        except Exception as e:
            print(f"Attempt {i+1}: Exception occurred - {str(e)}")
            if i < 20:  # Only attempt to swipe if it's not the last iteration
                print("Swiping to find 'Contact Us Button'")
                driver.swipe(333,967,354,850)#870
                driver.implicitly_wait(3)#2
            else:
                print("Element not found after maximum attempts")
            continue

timeout=90

#My Account 
my_account = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
)
my_account.click()
time.sleep(3) 
take_screenshot("myaccoont.png")
#Login inside my account
login= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Login')]"))  
)

login.click()
time.sleep(3)
screenshot_path = os.path.join(screenshot_dir, "Login2.png")
driver.save_screenshot(screenshot_path)


#Return from login
login_back = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

login_back.click()


#My Store Credit

my_store_credit = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'My Store Credit')]"))
)
my_store_credit.click()

time.sleep(2)
take_screenshot("My_Store_Credit.png")

return_from_mycredit = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_mycredit.click()



#Track Order
track_order = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Track Order')]"))  
)

track_order.click()
time.sleep(3)
take_screenshot("Track Order2.png")

return_from_trackorder = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_trackorder.click()




#Choose Language & Currency
choose_language = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Country Currency Button')]"))  
)

choose_language.click()
time.sleep(3)
take_screenshot("Language & Currency.png")


#Return from Lang & Currency
return_from_langandcurrency = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_langandcurrency.click()


button_xpath="//*[contains(@content-desc, 'Secure Shopping Button')]"
test_scroll(button_xpath)
print("get out of function")
time.sleep(2)
take_screenshot("secure_shop.png")

#Return from Secure Shopping

return_from_secure_shopping= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_secure_shopping.click()

#contact
button_xpath1="//*[contains(@content-desc, 'Contact Us Button')]"
test_scroll(button_xpath1)
print("get out of function2")
time.sleep(2)
take_screenshot("Contact_Us4.png")

#Return from Contact Us
return_from_contact_us = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_contact_us.click()

#Track Your order by guest
print("get out of code3")
button_xpath2="//*[contains(@content-desc, 'Track Order Guest Button')]"
test_scroll(button_xpath2)
print("get out of function3")
time.sleep(2)
take_screenshot("track_order.png")

#Return from Track order by guest
return_from_track_order_by_guest= WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_track_order_by_guest.click()

print("get out of code4")
button_xpath2="//*[contains(@content-desc, 'Affiliate') and contains(@content-desc, 'Program')]"
test_scroll(button_xpath2)
print("get out of function4")
time.sleep(2)
take_screenshot("Affilate_program.png")


return_from_affilate = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)

return_from_affilate.click()
time.sleep(5)
# influencer_registration
print("get out of code5")
button_xpath2="//*[contains(@content-desc, 'Influencer') and contains(@content-desc, 'Registration')]"
test_scroll(button_xpath2)
print("get out of function5")
time.sleep(2)
take_screenshot("Influencer_Registration.png")

#Return_from_influencer_registration
Return_from_influencer_registration = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
Return_from_influencer_registration.click()

# privacy policy
print("get out of code6")
button_xpath2="//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]"
test_scroll(button_xpath2)
print("get out of function6")
time.sleep(2)
take_screenshot("Privacy_Policy.png")
return_from_privacy_policy = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_privacy_policy.click()

print("get out of code7")
button_xpath2="//*[contains(@content-desc, 'Terms') and contains(@content-desc, 'Conditions')]"
test_scroll(button_xpath2)
print("get out of function7")
time.sleep(2)
take_screenshot("terms_condition.png")

return_from_terms_condn = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_terms_condn.click()

#shipping
print("get out of code8")
button_xpath2="//*[contains(@content-desc, 'Shipping') and contains(@content-desc,'Button')]"
test_scroll(button_xpath2)
print("get out of function8")
time.sleep(2)
take_screenshot("shipping.png")

return_from_shipping = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_shipping.click()

#Ticket_by_email
print("get out of code9")
button_xpath2="//*[contains(@content-desc, 'Track Your Ticket') and contains(@content-desc, 'By Email')]"
test_scroll(button_xpath2)
print("get out of function9")
time.sleep(2)
take_screenshot("track_by_email.png")

return_track_by_email = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_track_by_email.click()

#about us

print("get out of code10")
button_xpath2="//*[contains(@content-desc, 'About Us') and contains(@content-desc,'Button')]"
test_scroll(button_xpath2)
print("get out of function10")
time.sleep(2)
take_screenshot("about_us.png")

return_about_us = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_about_us.click()

#refer a friend
print("get out of code11")
button_xpath2="//*[contains(@content-desc, 'Refer A Friend') and contains(@content-desc, 'And Earn Discount')]"
test_scroll(button_xpath2)
print("get out of function11")
time.sleep(2)

take_screenshot("refer_friend.png")

return_refer_friend = WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_refer_friend.click()

#returns and refunds
print("get out of code12")
button_xpath2="//*[contains(@content-desc, 'Returns') and contains(@content-desc, 'And Refunds')]"
test_scroll(button_xpath2)
print("get out of function12")
time.sleep(2)
take_screenshot("return_and_refund.png")

return_and_refund= WebDriverWait(driver, timeout).until(
     EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_and_refund.click()


#Cart
cart_icon = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 4"))
)
cart_icon.click()

time.sleep(3)
take_screenshot("Cart.png")


#Designer
Designer_icon = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 1"))
)
Designer_icon.click()

time.sleep(3)
take_screenshot("Designer.png")

menu_icon = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Dashboard Drawer Icon')]"))
)
menu_icon.click()
take_screenshot("menu.png")
time.sleep(2)  # Allow time for the menu to fully open
# Women section
women_section = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'Women')]"))
)
women_section.click()

all_women_section = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'All Women')]"))
)
all_women_section.click()
time.sleep(3)
take_screenshot("women.png")

# Navigate back
back_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
)
back_button.click()
# Men section
men_btn = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'Men') and contains(@content-desc, 'item')]"))
)
men_btn.click()
all_men_section = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'All Men')]"))
)
all_men_section.click()
time.sleep(3)
take_screenshot("men.png")

# Navigate back
click_back1_button(driver)
# Kids section
kids_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'Kids')]"))
)
kids_btn.click()
all_kids_section = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Drawer') and contains(@content-desc, 'All Kids')]"))
)
all_kids_section.click()
time.sleep(3)
take_screenshot("kids.png")
# Navigate back
click_back1_button(driver)

