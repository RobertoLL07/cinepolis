from selenium import webdriver
from page_object_models.home_page import CinepolisHome, MoviesPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == '__main__':
    s = Service(executable_path='./drivers/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    mainPage = CinepolisHome(driver)
    mainPage.load()
    mainPage.cities()
    mainPage.complexes()

    movieSelect = MoviesPage(driver)
    movieSelect.program()


    try:
        element = WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root"]/div[1]/section/section/div/div/div[1]/h3'), 'Selecciona tus boletos')
        )

        actual_text = element.text
        print(f"Expected text is visible: {actual_text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()








