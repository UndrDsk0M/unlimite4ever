import logging
from time import sleep
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

edge_options = Options()
edge_options.add_argument("--headless")
edge_options.add_argument("disable-gpu")

class AI:
    def __init__(self, driver=Edge(options=edge_options)):
        """Driver gets an selenium.webdriver (Defualt using edge)
        """
        self.url = "https://replicate.com/blog/run-llama-3-with-an-api?utm_source=project&utm_campaign=llama2ai"
        self.driver = driver
        self.driver.get(self.url)

    def chat(self, prompt):
        """give a prompt and wait to get an awnser 
        This func start a edge (or other drivers you give) to llama3 website and control it to put prompt and get response (by selenium) 
        \nx = Ai.chat(prompt)
        \nprint(x) # wait plz (about 5sec to 5min)
        """
        try:
            element = self.driver.find_element(By.ID ,"prompt")
            action = ActionChains(self.driver)
            action.click(on_element = element)
            action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
            action.send_keys(prompt).send_keys(Keys.RETURN).perform()

            status = 1
            while status:
                try:
                    self.driver.find_element(By.CLASS_NAME, 'w-4')
                    status = status + 1 if status <= 3 else 1
                    logger.info(f"Loading{'.'*status}")
                    sleep(0.1)
                except:
                    status = False

            return self.driver.find_element(By.CSS_SELECTOR, 'div.output').text
        except Exception as e:
            raise e

    def close(self):
        self.driver.quit()

def main():
    ai = AI()
    result = ai.chat(input("- Chat with AI: "))
    print('+ '+result)
    ai.close()

if __name__ == "__main__":
    main()

