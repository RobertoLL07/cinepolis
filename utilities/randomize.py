from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from random import choice, randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def randomizeCC(driver, element): #Randomize the City and Complex
    option = driver.find_element(*element)
    options = option.find_elements(By.TAG_NAME, 'option')[1:]
    final_rand = choice(options).text
    printing = Select(option)
    printing.select_by_visible_text(final_rand)
    return final_rand


def randomizeMH(driver): #Randomize the Movie and Hour
    links = driver.find_elements(By.TAG_NAME, 'time')
    specific_text = 'locationHide'
    filtered_links = []

    for link in links:
        divs = link.find_elements(By.XPATH, './ancestor::div')
        divs_with_specific_text = [div for div in divs if specific_text in div.get_attribute('class')]

        if not divs_with_specific_text:
            filtered_links.append(link)

    if filtered_links:
        random_index = random.randint(0, len(links) - 1)
        selected_link = links[random_index]
        #selected_link.click()

    for attempt in range(len(links)):
        try:
            element = WebDriverWait(driver, .1).until(EC.element_to_be_clickable(selected_link))
            element.click()
            break

        except Exception as e:
            print(f"Attempt {attempt + 1}: No clickable button")

    ad_element = (By.ID, 'dismiss-button')

    try:
        ad = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(ad_element))

        if ad.is_displayed():
            ad.click()
        else:
            print("The element is not visible after waiting.")
            pass
    except:
        pass
