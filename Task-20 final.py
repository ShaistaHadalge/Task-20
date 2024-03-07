#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)

# Navigate to the Cowin website
driver.get("https://www.cowin.gov.in/")

# Click on "FAQ" link to open a new window
driver.find_element(By.LINK_TEXT, "FAQ").click()

#time delay
time.sleep(4)

# Click on "Partners" link to open another new window
driver.find_element(By.XPATH, "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a").click()

#time delay
time.sleep(4)

# Get the handles of all open windows
window_handles = driver.window_handles

# Display window/frame IDs in the console
for handle in window_handles:
    driver.switch_to.window(handle)
    print(f"Window/Frame ID: {handle}")
# Close the two new windows and switch back to the original window
for handle in window_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()
# Switch back to the original window
driver.switch_to.window(window_handles[0])

# Perform any additional actions on the original window if needed
#time delay
time.sleep(4)

# Close the original window
driver.close()



# In[3]:


from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.cowin.gov.in/")
parent=driver.current_window_handle
print("parent window is",parent)
time.sleep(4)
driver.maximize_window()
time.sleep(5)
from selenium.webdriver.common.by import By
time.sleep(5)
driver.find_element(By.LINK_TEXT,"FAQ").click()
time.sleep(5)
window1=driver.current_window_handle
print("first window handle id is",window1)
driver.find_element(By.LINK_TEXT,"PARTNERS").click()
window2=driver.current_window_handle
print("second window handle id is",window2)
time.sleep(5)
all=driver.window_handles
print(all)
for i in all:
    if i!=parent:
        driver.switch_to.window(i)
        time.sleep(5)
        driver.close()
        time.sleep(5)






# In[7]:


from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://labour.gov.in/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"open_button").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Documents").click()
time.sleep(5)
download=driver.find_element(By.XPATH,"//*[@id='fontSize']/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/a")
time.sleep(5)
download.click()
time.sleep(5)
a=driver.switch_to.alert
time.sleep(5)
a.accept()
time.sleep(10)


# In[5]:


from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://labour.gov.in/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"open_button").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Documents").click()
time.sleep(5)
download=driver.find_element(By.XPATH,"//*[@id='fontSize']/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/a")
time.sleep(5)
download.click()
time.sleep(5)
a=driver.switch_to.alert
time.sleep(5)
a.accept()
time.sleep(10)


# In[8]:


path1=r"C:\Users\shais\OneDrive\Desktop\Sample\screenshot.png"#path1 location specified
#path12=r"C:\Users\shais\OneDrive\Desktop\Sample\screenshot.docx"
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
driver.get("https://labour.gov.in/photo-gallery")#opening the gallery page from the labour.gov.in website
#driver.find_element(By.CLASS_NAME,"open_button").click()
#driver.implicitly_wait(10)
#driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"Media").click()
#time.sleep(10)
#driver.find_element(By.CLASS_NAME,"menu__link").click()
#time.sleep(10)
driver.maximize_window()#maximising the website window
driver.execute_script("window.scrollTo(0,500);")#getting to scroll the website page
driver.save_screenshot(path1)#saving the got screenshot in specified path which is mentioned in the path1 variable
time.sleep(3)#waiting in the webpage until the specified number of seconds using sleep method
print("check the screenshot of the page in path1 ")


# In[ ]:




