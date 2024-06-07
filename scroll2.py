from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import os
from selenium.webdriver.common.by import By
import pdb
import time
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

timeout = 90

# My Account
my_account = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
)
time.sleep(5)
my_account.click()
# pdb.set_trace()
time.sleep(10)

# window_size = driver.get_window_size()
# start_x = window_size['width'] // 2
# start_y = int(window_size['height'] * 0.2)
# end_y = int(window_size['height'] * 0.8)
# driver.swipe(start_x, start_y, start_x, end_y, 1000)
# el1 = driver.find_element(By.XPATH,"//*[contains(@content-desc, 'My Store Credit')]")
# time.sleep(5)
# el2 = driver.find_element(By.XPATH, "//*[contains(@content-desc, 'Track Order')]")
# action = TouchAction(driver)
# action.press(el1).move_to(el2).release().perform()
def is_element_in_view(element):
    # Get the window size
    window_size = driver.get_window_size()
    window_height = window_size['height']
    print(window_height)
    window_width = window_size['width']
    
    # Get the element location and size
    element_location = element.location
    element_size = element.size
    
    # Calculate element bounds
    element_top = element_location['y']
    element_bottom = element_top + element_size['height']
    element_left = element_location['x']
    element_right = element_left + element_size['width']
    
    # Check if element is within the screen bounds
    if element_top >= 20 and element_bottom <= window_height-30 and \
       element_left >= 10 and element_right <= window_width-10:
        print("elemnent is in view now you can click")
        return True
    else:
        print("entered into else")
        return False

def test_scroll(button_xpath):
    time.sleep(3)
    i=0
    for i in range(20):
        try:
            print(f"Attempt {i+1}: Trying to find 'Contact Us Button'")
            contact_us = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, button_xpath))
            )
            output=is_element_in_view(contact_us)
            if(output==True):
                 
                print("Element found, clicking 'Contact Us Button'")
                contact_us.click()
            
                break
        except Exception as e:
            print(f"Attempt {i+1}: Exception occurred - {str(e)}")
            if i < 20:  # Only attempt to swipe if it's not the last iteration
                print("Swiping to find 'Contact Us Button'")
                driver.swipe(333,967,354,890)#870
                driver.implicitly_wait(2)
            else:
                print("Element not found after maximum attempts")
            continue

# Call the test_scroll function
button_xpath="//*[contains(@content-desc, 'Secure Shopping Button')]"
test_scroll(button_xpath)
print("get out of function")
time.sleep(2)
screenshot_path = os.path.join(screenshot_dir, "Contact Us3.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Contact Us
return_from_contact_us = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_contact_us.click()
print("get out of code1")
time.sleep(2)
button_xpath1="//*[contains(@content-desc, 'Contact Us Button')]"
test_scroll(button_xpath1)
print("get out of function2")
time.sleep(2)
screenshot_path = os.path.join(screenshot_dir, "Contact Us4.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Contact Us
return_from_contact_us = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_contact_us.click()
time.sleep(3)
print("get out of code3")
button_xpath2="//*[contains(@content-desc, 'Track Your Ticket') and contains(@content-desc, 'By Email')]"
test_scroll(button_xpath2)
print("get out of function3")
time.sleep(2)
screenshot_path = os.path.join(screenshot_dir, "Contact Us5.png")
driver.save_screenshot(screenshot_path)
time.sleep(5)

#Return from Contact Us
return_from_contact_us = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='android.widget.Button']"))  
)
return_from_contact_us.click()
print("get out of code3")
# time.sleep(20)


# def scroll_down_menu_settings(driver, distance=400):
#     action = ActionChains(driver)
#     window_size = driver.get_window_size()
#     x, y = window_size['width'] / 6, window_size['height'] / 2

#     # Create the pointer input for touch actions
#     pointer_input = PointerInput(PointerInput.TOUCH, "touch")
#     actions = ActionBuilder(driver, mouse=pointer_input)
#     actions.pointer_action.move_to_location(x, y)
#     actions.pointer_action.pointer_down()
#     actions.pointer_action.move_to_location(x, y - distance)
#     actions.pointer_action.pointer_up()
#     actions.perform()

# # Call the function
# scroll_down_menu_settings(driver, distance=400)

# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# import os
# import time
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# # from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # from appium.webdriver.common.mobileby import MobileBy, AppiumBy
# # from appium.webdriver.common.mobileby import MobileBy
# # Desired Capabilities
# cap: Dict[str, Any] = {
#     "platformName": "Android",
#     "platformVersion": "13.0",
#     "deviceName": "Galaxy_Nexus_API_34",
#     "app": "C:\\Users\\Admin\\APk_enable\\app_two_prod_debug_30_05.apk"  # Path to your APK file
# }

# # Appium server URL
# url = 'http://localhost:4723/wd/hub'

# # Initialize the WebDriver
# driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# screenshot_dir = r"C:\Users\Admin\PycharmProjects\pythonProject\screenshots"
# # Create the directory if it doesn't exist
# if not os.path.exists(screenshot_dir):
#     os.makedirs(screenshot_dir)

# timeout=90

# # My Account
# my_account = WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
# )
# my_account.click()
# def scroll_down_menu_settings(driver, distance=400):
#     action = ActionChains(driver)
#     window_size = driver.get_window_size()
#     x, y = window_size['width'] / 6, window_size['height'] / 2
#     action.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
#     action.w3c_actions.pointer_action.move_to_location(x, y)
#     action.w3c_actions.pointer_action.click_and_hold()
#     action.w3c_actions.pointer_action.move_to_location(x, y - distance)
#     action.w3c_actions.pointer_action.release()
#     action.w3c_actions.perform()

# # Call the function
# scroll_down_menu_settings(driver, distance=400)

# element_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Secure").instance(0))')
# element=WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Secure Shopping Button')]"))  
# )
# element.click()
# def s
# croll_down_using_ui_scrollable(driver, element_text):
#     # Find a scrollable element using UiSelector
#     scrollable_element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
#         "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView("
#         + "new UiSelector().text(\"" + element_text + "\"))")
#     scrollable_element.click()
#     # Perform the scrolling action
#     # scroll_down_using_ui_scrollable()
# scroll_down_using_ui_scrollable(driver, "Secure")
# time.sleep(4)
# # Specify the locator of the element you want to interact with
# element_locator = (By.XPATH, "//*[contains(@content-desc, 'Secure Shopping Button')]")

# # Maximum number of scroll attempts
# max_scroll_attempts = 5
# scroll_attempt = 0
# element = None

# while scroll_attempt < max_scroll_attempts:
#     try:
#         # Try to locate the element
#         element = WebDriverWait(driver, timeout).until(
#             EC.presence_of_element_located(element_locator)
#         )
#         # If element is found, break the loop
#         break
#     except TimeoutException:
#         # If element is not found, perform scrolling
#         actions = [
#             {"type": "pointer", "id": "finger1", "parameters": {"pointerType": "touch"}, "actions": [
#                 {"type": "pointerMove", "origin": "viewport", "x": 100, "y": 100},
#                 {"type": "pointerDown", "button": 0},
#                 {"type": "pause", "duration": 500},
#                 {"type": "pointerMove", "origin": "viewport", "x": 200, "y": 200},
#                 {"type": "pointerUp", "button": 0}
#             ]}
#         ]
#         driver.execute_script('mobile: performActions', {'actions': actions})
#         scroll_attempt += 1

# # Check if element is found after scrolling
# if element:
#     # Click on the element
#     element.click()
# else:
#     print("Element not found after scrolling.")


# element_locator = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Secure Shopping Button ")')
# element=WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Secure Shopping Button')]"))  
# )
# actions = [
#     {"action": "press", "x": 100, "y": 100},
#     {"action": "moveTo", "x": 200, "y": 200},
#     {"action": "release"}
# ]
# driver.execute_script('mobile: performActions', {'actions': actions})

# Perform actions using W3C WebDriver actions
# actions = [
#     {"action": "press", "x": 100, "y": 100},
#     {"action": "moveTo", "x": 200, "y": 200},
#     {"action": "release"}
# ]
# driver.execute_script('mobile: performActions', {'actions': actions})
# def scroll_to_element(driver, element):
#     # Get the dimensions of the device screen
#     width = driver.get_window_size()['width']
#     height = driver.get_window_size()['height']

#     # Set the starting and ending points for the scroll
#     start_x = width // 2
#     start_y = int(height * 0.8)  # Start from 80% down the screen
#     end_y = int(height * 0.2)    # End at 20% down the screen

#     # Perform the scroll until the element is found or maximum scrolls reached
#     max_scrolls = 10  # Adjust as needed
#     scrolls = 0
#     while scrolls < max_scrolls:
#         try:
#             driver.find_element(*element).is_displayed()
#             break  # Element found, exit loop
#         except NoSuchElementException:
#             # Element not found, perform scroll
#             action = TouchAction(driver)
#             action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()
#             scrolls += 1
#     else:
#         raise NoSuchElementException(f"Element {element} not found after {max_scrolls} scrolls")

# # Example usage:
# # Specify the locator of the element you want to scroll to
# element_locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Secure Shopping Button ")')
# # Scroll to the element
# scroll_to_element(driver, element_locator)
