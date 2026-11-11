from selenium.webdriver.common.by import By




username = driver.find_element(By.ID, "username")

# List of all matching elements; empty if none

inputs = driver.find_elements(By.TAG_NAME, "input")

print(len(inputs))