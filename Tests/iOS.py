from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "iOS"
caps["appium:platformVersion"] = "15.5"
caps["appium:deviceName"] = "iPhone 8 Plus"
caps["appium:app"] = "/Users/qups/Downloads/Python-Appium-App-Page-Object-Model-BD-Jobs-main/iOSPythonAppium/APP/UICatalog.app"
caps["appium:automationName"] = "XCUITest"
caps["appium:noReset"] = "true"
caps["appium:includeSafariInWebviews"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


driver.quit()