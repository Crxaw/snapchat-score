import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class snapchat:
    def __init__(self, path_delay=0.25, driver_arguments=[]):
        
        self.path_delay = path_delay
        self.driver_arguments = ["--window-size=1920,1080", "--disable-gpu", "--start-maximized", "--no-sandbox", f"--user-data-dir={os.path.join(os.path.dirname(__file__), 'driver')}"]
        self.driver_arguments.extend(driver_arguments)
        
        self.paths = {"friends": {"path": "FiLwP", "path_type": "classpath"}, "send_snaps": {"path": "HEkDJ", "path_type": "classpath"}, "take_snap": {"path": "UEYhD", "path_type": "classpath"}, "confirm_snap": {"path": "/html/body/div[4]/div/div/div/div/div/div/div[2]/div/form/div[2]/button", "path_type": "xpath"}}
        
        
    def return_element(self, driver, path, type="xpath"):
        if type == "xpath":
            return WebDriverWait(driver, self.path_delay).until(EC.visibility_of_all_elements_located((By.XPATH, path)))
        elif type == "classpath":
            return WebDriverWait(driver, self.path_delay).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, path)))
        else:
            raise ValueError("Unkown type")
            
    def driver(self):
        options = webdriver.ChromeOptions()
        for option in self.driver_arguments:
            options.add_argument(option)
            
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        driver.get("https://web.snapchat.com/")
        return driver
    
    def farm_points(self):
        driver = self.driver()
        # friends = self.return_element(driver, self.paths["friends"]["path"], self.paths["friends"]["path_type"])
        # for user in [user for user in friends if friends[-1].text != user.text]:
        #      ActionChains(driver).click(user).perform()
        time.sleep(5)
        action_chains = ActionChains(driver)
        html_element = driver.find_element(By.TAG_NAME, "html")
        action_chains.move_to_element_with_offset(html_element, 0, 0).click().perform()
        send_snaps = self.return_element(driver, self.paths["send_snaps"]["path"], self.paths["send_snaps"]["path_type"])
        for i in range(25):
         for snap in send_snaps.copy():
          try:
            snap.click()
            time.sleep(0.5)
            button = random.choice(self.return_element(driver, self.paths["take_snap"]["path"], self.paths["take_snap"]["path_type"]))
            button.click()
            time.sleep(0.5)
            button = random.choice(self.return_element(driver, self.paths["confirm_snap"]["path"], self.paths["confirm_snap"]["path_type"]))
            button.click()
          except:
              action_chains = ActionChains(driver)
              html_element = driver.find_element(By.TAG_NAME, "html")
              action_chains.move_to_element_with_offset(html_element, 0, 0).click().perform()
              continue
        time.sleep(60)
        
    
        
                

snapchat = snapchat()
while True:
    snapchat.farm_points()
