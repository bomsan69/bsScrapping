from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from Parse import Parse
from bs4 import BeautifulSoup as bs

def Scrapping(keyword):

    #Create a Chrome web driver and setting the options
    chrome_options = Options()


    #keep the browser window open until the user closes it
    chrome_options.add_experimental_option("detach", True)


    #instantiating the driver
    driver = webdriver.Chrome(options= chrome_options)

    action = ActionChains(driver)


    #setting the url
    url = "https://www.homedepot.com/s/"+keyword
    driver.get(url)

    time.sleep(3)

    action.move_to_element(driver.find_element(By.CSS_SELECTOR, 'nav.hd-pagination')).perform()

    time.sleep(3)


    html=driver.page_source;

 #   with open('heom.txt', 'w') as f:
 #       f.write(html)
    


    product_list = Parse(html)

    print(product_list)
    print("len of product list\n")
    print(len(product_list))
    
    driver.quit()



if __name__ == "__main__":
    Scrapping("drill")
  
  

