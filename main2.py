from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')  # Required for running as root
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resources
chrome_options.add_argument('--disable-gpu')  # Optional for better performance
chrome_options.add_argument('--remote-debugging-port=9222')  # Avoid DevToolsActivePort issue

# Initialize ChromeDriver with options
driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"), options=chrome_options)

# Example action
driver.get("https://www.google.com")
print("Page title:", driver.title)
driver.quit()
