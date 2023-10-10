from selenium.webdriver.common.by import By
from utilities.randomize import randomizeCC, randomizeMH


class CinepolisHome:
    url = 'https://cinepolis.com/'
    city = (By.ID, 'cmbCiudades')
    complex = (By.ID, 'cmbComplejos')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)

    def cities(self):
        randomizeCC(self.driver, self.city)

    def complexes(self):
        randomizeCC(self.driver, self.complex)


class MoviesPage:

    def __init__(self, driver):
        self.driver = driver

    def program(self):
        randomizeMH(self.driver)





