from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, os
from selenium.webdriver.common.action_chains import ActionChains

def clear_tabs() -> None:
    # Assuming driver is your WebDriver instance
    # Get the handles of all open windows
    all_handles = driver.window_handles

    # Get the handle of the main window
    main_window_handle = driver.current_window_handle

    # Close all tabs except the main one
    for handle in all_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            driver.close()

    # Switch back to the main window
    driver.switch_to.window(main_window_handle)

def navigate(site) -> None: # Uses unconventional method to bypass anti bots.
    driver.execute_script(f"window.open('{site}')")
    driver.switch_to.window(window_name=driver.window_handles[0])   # switch to first tab
    driver.close()
    driver.switch_to.window(window_name=driver.window_handles[0] )  # switch back to new tab
    print(driver.title)
    if 'Just a moment' in driver.title:
        print("Cloudflare has been detected")
        cloudflare()

# Experimental cloudflare bypass
def cloudflare():
    time.sleep(10)
    iframe = driver.find_element(By.XPATH, ('//iframe'))
    driver.switch_to.frame(iframe)
    print(iframe)
    element = driver.find_elements(By.XPATH, ("//input[@type='checkbox']"))
    actions = ActionChains(driver)
    actions.move_to_element(element[0])
    actions.click()
    #element[0].click()
    print(element)
    input()
    element[0].click()

if __name__ == "__main__":
    chrome_options = Options()
    
    # Custom chromedriver, browser and user data path
    chrome_options.binary_location = os.path.dirname(os.path.realpath(__file__)) + "\\chrome\\chrome.exe" # Change to browser binary path
    chrome_service = Service('chromedriver.exe')
    # Set chrome user data on the project folder. It should be named 'data_dir'.
    chrome_options.add_argument('--user-data-dir=' + os.path.dirname(os.path.realpath(__file__)) + '\\data_dir')
    
    # Add proxy capabilities
    use_proxy = False
    if(use_proxy == True):
        # Change to appropriate values.
        proxy = 'proxy-server.com:1080' 
        chrome_options.add_argument('--proxy-server=socks5://' + proxy)
        print("Proxy is enabled.")  
    
    
    
    # Bypass Selenium Detection
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    # Remove "profile.managed_default_content_settings.images" if you wish to enable images. Disabled on default to save bandwidth.
    prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            'disk-cache-size': 4096,
            "profile.managed_default_content_settings.images": 2
        }
    chrome_options.add_experimental_option("prefs", prefs)
    
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("--remote-debugging-port=9223")
    chrome_options.add_argument("--disable-3d-apis")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--no-sandbox");
    chrome_options.add_argument("--disable-dev-shm-usage");
    chrome_options.add_argument("--disable-renderer-backgrounding");
    chrome_options.add_argument("--disable-background-timer-throttling");
    chrome_options.add_argument("--disable-backgrounding-occluded-windows");
    chrome_options.add_argument("--disable-client-side-phishing-detection");
    chrome_options.add_argument("--disable-crash-reporter");
    chrome_options.add_argument("--disable-oopr-debug-crash-dump");
    chrome_options.add_argument("--no-crash-upload");
    chrome_options.add_argument("--disable-gpu");
    #chrome_options.add_argument("--disable-extensions");
    chrome_options.add_argument("--disable-low-res-tiling");
    chrome_options.add_argument("--log-level=3");
    
    
    # Initiate selenium driver
    driver = webdriver.Chrome(options=chrome_options)
    clear_tabs()
    
    navigate("https://google.com")
    time.sleep(5)
    print("Done")
