# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import time
# from selenium.webdriver.common.by import By
# from appium import webdriver
# import pdb
# # from appium.webdriver.common.mobileby import MobileBy
# # from selenium.common.exceptions import NoSuchElementException    

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
#      os.makedirs(screenshot_dir)

# def take_screenshot(name):
#     screenshot_path = os.path.join(screenshot_dir, name)
#     driver.save_screenshot(screenshot_path)
    
# def click_back1_button(driver):
#         retries = 3  # Number of retries
#         for _ in range(retries):
#          try:
#             back_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
#             )
#             back_button.click()
#             return
#          except StaleElementReferenceException:
#             print("StaleElementReferenceException caught. Retrying...")

# # def scroll_until_element_visible():
# #     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
# #     'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward(2)'
# #  )
# # def scroll_until_element_visible(driver, by, value):
# #     while True:
# #         try:
# #             element = driver.find_element(by, value)
# #             pdb.set_trace()
# #             return element
# #         except NoSuchElementException:
#             # Scroll down
          
               
# timeout=90

# #My Account 

# my_account = WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((By.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
# )
# my_account.click()

# time.sleep(10) 
# #privacy policy
# # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
# #     'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward(3)'
# # )
# # element = driver.find_element(AppiumBy.XPATH,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("Privacy Policy Button")')
# # driver.findElementByAndroidUIAutomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"Privacy\").instance(0))").click()
# element = appium_driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
#         'new UiScrollable(new UiSelector().scrollable(true).index(0)).scrollIntoView(new UiSelector().textContains(\"Privacy\"))')

# pdb.set_trace()
# privacy_policy = WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]"))
# )
# privacy_policy = scroll_until_element_visible(driver, AppiumBy.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]")

# privacy_policy.click()
# # # # time.sleep(5)
# # # # take_screenshot("Privacy_Policy.png")
# # # from appium import webdriver
# # # from typing import Any, Dict
# # # from appium.options.common import AppiumOptions
# # # from appium.webdriver.common.appiumby import AppiumBy
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# # # import os
# # # import time

# # # # Desired Capabilities
# # # cap: Dict[str, Any] = {
# # #     "platformName": "Android",
# # #     "platformVersion": "13.0",
# # #     "deviceName": "Galaxy_Nexus_API_34",
# # #     "app": "C:\\Users\\Admin\\APk_enable\\app_two_prod_debug_30_05.apk"  # Path to your APK file
# # # }

# # # # Appium server URL
# # # url = 'http://localhost:4723/wd/hub'

# # # # Initialize the WebDriver
# # # driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# # # screenshot_dir = r"C:\Users\Admin\PycharmProjects\pythonProject\screenshots"
# # # # Create the directory if it doesn't exist
# # # if not os.path.exists(screenshot_dir):
# # #     os.makedirs(screenshot_dir)

# # # def take_screenshot(name):
# # #     screenshot_path = os.path.join(screenshot_dir, name)
# # #     driver.save_screenshot(screenshot_path)

# # # def click_back1_button(driver):
# # #     retries = 3  # Number of retries
# # #     for _ in range(retries):
# # #         try:
# # #             back_button = WebDriverWait(driver, 10).until(
# # #                 EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
# # #             )
# # #             back_button.click()
# # #             return
# # #         except StaleElementReferenceException:
# # #             print("StaleElementReferenceException caught. Retrying...")

# # # def scroll_by_percentage(driver, start_percentage, end_percentage, anchor_percentage):
# # #     size = driver.get_window_size()
# # #     width = size['width']
# # #     height = size['height']
# # #     anchor = int(width * anchor_percentage)
# # #     start_point = int(height * start_percentage)
# # #     end_point = int(height * end_percentage)
    
# # #     actions = TouchAction(driver)
# # #     actions.press(x=anchor, y=start_point) \
# # #         .wait(ms=1000) \
# # #         .move_to(x=anchor, y=end_point) \
# # #         .release() \
# # #         .perform()

# # # def scroll_until_element_visible(driver, by, value, max_scrolls=5):
# # #     scroll_attempts = 0
# # #     while scroll_attempts < max_scrolls:
# # #         try:
# # #             element = driver.find_element(by, value)
# # #             return element
# # #         except NoSuchElementException:
# # #             scroll_by_percentage(driver, 0.8, 0.2, 0.5)
# # #             scroll_attempts += 1
# # #     raise NoSuchElementException(f"Element with {by} and value {value} not found after {max_scrolls} scrolls")

# # # timeout = 90

# # # # My Account
# # # my_account = WebDriverWait(driver, timeout).until(
# # #     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
# # # )
# # # my_account.click()

# # # time.sleep(10)

# # # # Privacy Policy
# # # privacy_policy = scroll_until_element_visible(driver, AppiumBy.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]")
# # # privacy_policy.click()

# # # time.sleep(5)
# # # take_screenshot("Privacy_Policy.png")

# # from appium import webdriver
# # from typing import Any, Dict
# # from appium.options.common import AppiumOptions
# # from appium.webdriver.common.appiumby import AppiumBy
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# # from appium.webdriver.common.touch_action import TouchAction
# # import os
# # import time

# # # Desired Capabilities
# # cap: Dict[str, Any] = {
# #     "platformName": "Android",
# #     "platformVersion": "13.0",
# #     "deviceName": "Galaxy_Nexus_API_34",
# #     "app": "C:\\Users\\Admin\\APk_enable\\app_two_prod_debug_30_05.apk"  # Path to your APK file
# # }

# # # Appium server URL
# # url = 'http://localhost:4723/wd/hub'

# # # Initialize the WebDriver
# # driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# # screenshot_dir = r"C:\Users\Admin\PycharmProjects\pythonProject\screenshots"
# # # Create the directory if it doesn't exist
# # if not os.path.exists(screenshot_dir):
# #     os.makedirs(screenshot_dir)

# # def take_screenshot(name):
# #     screenshot_path = os.path.join(screenshot_dir, name)
# #     driver.save_screenshot(screenshot_path)

# # def click_back1_button(driver):
# #     retries = 3  # Number of retries
# #     for _ in range(retries):
# #         try:
# #             back_button = WebDriverWait(driver, 10).until(
# #                 EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
# #             )
# #             back_button.click()
# #             return
# #         except StaleElementReferenceException:
# #             print("StaleElementReferenceException caught. Retrying...")

# # def scroll_by_percentage(driver, start_percentage, end_percentage, anchor_percentage):
# #     size = driver.get_window_size()
# #     width = size['width']
# #     height = size['height']
# #     anchor = int(width * anchor_percentage)
# #     start_point = int(height * start_percentage)
# #     end_point = int(height * end_percentage)
    
# #     actions = TouchAction(driver)
# #     actions.press(x=anchor, y=start_point) \
# #         .wait(ms=1000) \
# #         .move_to(x=anchor, y=end_point) \
# #         .release() \
# #         .perform()

# # def scroll_until_element_visible(driver, by, value, max_scrolls=5):
# #     scroll_attempts = 0
# #     while scroll_attempts < max_scrolls:
# #         try:
# #             element = driver.find_element(by, value)
# #             return element
# #         except NoSuchElementException:
# #             scroll_by_percentage(driver, 0.8, 0.2, 0.5)
# #             scroll_attempts += 1
# #     raise NoSuchElementException(f"Element with {by} and value {value} not found after {max_scrolls} scrolls")

# # timeout = 90

# # # My Account
# # my_account = WebDriverWait(driver, timeout).until(
# #     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
# # )
# # my_account.click()

# # time.sleep(10)

# # # Privacy Policy
# # privacy_policy = scroll_until_element_visible(driver, AppiumBy.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]")
# # privacy_policy.click()

# # time.sleep(5)
# # take_screenshot("Privacy_Policy.png")
# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# import os
# import time

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

# def take_screenshot(name):
#     screenshot_path = os.path.join(screenshot_dir, name)
#     driver.save_screenshot(screenshot_path)

# def click_back1_button(driver):
#     retries = 3  # Number of retries
#     for _ in range(retries):
#         try:
#             back_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
#             )
#             back_button.click()
#             return
#         except StaleElementReferenceException:
#             print("StaleElementReferenceException caught. Retrying...")

# def scroll_by_percentage(driver, start_percentage, end_percentage, anchor_percentage):
#     size = driver.get_window_size()
#     width = size['width']
#     height = size['height']
#     anchor = int(width * anchor_percentage)
#     start_point = int(height * start_percentage)
#     end_point = int(height * end_percentage)

#     actions = ActionBuilder(driver)
#     pointer = PointerInput(PointerInput.INTERACTION_TOUCH, "touch")
    
#     actions.add_action(pointer.create_pointer_move(0, 'viewport', x=anchor, y=start_point))
#     actions.add_action(pointer.create_pointer_down(PointerInput.MouseButton.LEFT))
#     actions.add_action(pointer.create_pause(1))  # Adjust the pause duration as needed
#     actions.add_action(pointer.create_pointer_move(0, 'viewport', x=anchor, y=end_point))
#     actions.add_action(pointer.create_pointer_up(PointerInput.MouseButton.LEFT))

#     actions.perform()

# def scroll_until_element_visible(driver, by, value, max_scrolls=5):
#     scroll_attempts = 0
#     while scroll_attempts < max_scrolls:
#         try:
#             element = driver.find_element(by, value)
#             return element
#         except NoSuchElementException:
#             scroll_by_percentage(driver, 0.8, 0.2, 0.5)
#             scroll_attempts += 1
#     raise NoSuchElementException(f"Element with {by} and value {value} not found after {max_scrolls} scrolls")

# timeout = 90

# # My Account
# my_account = WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
# )
# my_account.click()

# time.sleep(10)

# # Privacy Policy
# privacy_policy = scroll_until_element_visible(driver, AppiumBy.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]")
# privacy_policy.click()

# time.sleep(5)
# take_screenshot("Privacy_Policy.png")


# from appium import webdriver
# from typing import Any, Dict
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# import os
# import time

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

# def take_screenshot(name):
#     screenshot_path = os.path.join(screenshot_dir, name)
#     driver.save_screenshot(screenshot_path)

# def click_back1_button(driver):
#     retries = 3  # Number of retries
#     for _ in range(retries):
#         try:
#             back_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//*[contains(@content-desc, 'App bar leading back button')]"))
#             )
#             back_button.click()
#             return
#         except StaleElementReferenceException:
#             print("StaleElementReferenceException caught. Retrying...")

# def scroll_by_percentage(driver, start_percentage, end_percentage, anchor_percentage):
#     size = driver.get_window_size()
#     width = size['width']
#     height = size['height']
#     anchor = int(width * anchor_percentage)
#     start_point = int(height * start_percentage)
#     end_point = int(height * end_percentage)

#     actions = ActionBuilder(driver)
#     pointer = PointerInput(PointerInput.INTERACTION_TOUCH, "touch")
    
#     actions.add_action(pointer.create_pointer_move(0, 'viewport', x=anchor, y=start_point))
#     actions.add_action(pointer.create_pointer_down(PointerInput.MouseButton.LEFT))
#     actions.add_action(pointer.create_pause(1))  # Adjust the pause duration as needed
#     actions.add_action(pointer.create_pointer_move(0, 'viewport', x=anchor, y=end_point))
#     actions.add_action(pointer.create_pointer_up(PointerInput.MouseButton.LEFT))

#     actions.perform()

# def scroll_until_element_visible(driver, by, value, max_scrolls=5):
#     scroll_attempts = 0
#     while scroll_attempts < max_scrolls:
#         try:
#             element = driver.find_element(by, value)
#             return element
#         except NoSuchElementException:
#             scroll_by_percentage(driver, 0.8, 0.2, 0.5)
#             scroll_attempts += 1
#     raise NoSuchElementException(f"Element with {by} and value {value} not found after {max_scrolls} scrolls")

# timeout = 90

# # My Account
# my_account = WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
# )
# my_account.click()

# time.sleep(10)

# # Privacy Policy
# privacy_policy = scroll_until_element_visible(driver, AppiumBy.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]")
# privacy_policy.click()

# time.sleep(5)
# take_screenshot("Privacy_Policy.png")
# def scroll_until_element_visible(driver, by, value):
#     while True:
#         try:
#             element = driver.find_element(by, value)
#             pdb.set_trace()
#             return element
#         except NoSuchElementException:
#             # Scroll down
#             river.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
#     'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollForward(2)'
# )
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
import os
import time
from appium.webdriver.common.mobileby import MobileBy, AppiumBy
# from appium.webdriver.common.mobileby import MobileBy
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
screenshot_dir = r"C:\Users\Admin\PycharmProjects\pythonProject\screenshots"
# Create the directory if it doesn't exist
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

timeout=90

# My Account
my_account = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Bottom Bar Svg Picture icon Tab 3"))
)
my_account.click()

time.sleep(4)

# Privacy Policy
#driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\"Privacy\").instance(0))").click()
description = "Privacy"
#scroll_command = f"new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
#                    f").textContains(\"{text}\").instance(0))"

# scroll_command = f"new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector(" \
#                     f").descriptionContains(\"{description}\").instance(0))"

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command).click()
element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().descriptionContains("Track Order Guest Button"))')
# track_order_by_guest = WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Track Order Guest Button')]"))  
# )

# track_order_by_guest.click()
element.click()
#privacy_policy = WebDriverWait(driver, timeout).until(
#    EC.presence_of_element_located((By.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]"))
#)
# privacy_policy = scroll_until_element_visible(driver, AppiumBy.XPATH, "//*[contains(@content-desc, 'Privacy') and contains(@content-desc, 'Policy')]")
#privacy_policy.click()

time.sleep(5)
# take_screenshot("Privacy_Policy.png")
