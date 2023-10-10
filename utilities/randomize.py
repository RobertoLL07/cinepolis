from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from random import choice, randint
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
        selected_link.click()
