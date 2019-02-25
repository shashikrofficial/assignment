from selenium import webdriver
from ConfigVars.TestConfig import Input
from ConfigVars.FrameworkConfig import urls,driverconfig
from os.path import dirname, join
import platform,time
import os


class DriverIntialization():

    baseURL = urls.HOME_PAGE

    def __init__(self,baseURL):
        # Define a variable to hold all the configurations needed
        chrome_options = webdriver.ChromeOptions()

        # Get Root Path Of the Project
        project_root = dirname(dirname(__file__))

        output_path = join(project_root, 'drivers')
        browser = driverconfig.BROWSER

        if browser == 'Firefox':
            if platform.system()=="Windows":
                # Path to firefox driver
                self.driver = webdriver.Firefox(executable_path=os.path.join(output_path,
                                                                             'firefox', 'geckodriver.exe'))

            elif platform.system() == "Darwin":
                # Path to firefox driver
                self.driver = webdriver.Firefox(executable_path=os.path.join(output_path,
                                                                             'firefox', 'geckodriver'))

        elif browser == "Chrome":
            if platform.system() == "Darwin":

                # Create driver, pass it the path to the chrome driver file and the
                # special configurations you want to run
                self.driver = webdriver.Chrome(executable_path=os.path.
                                               join(output_path, 'chrome', 'chromedriver'),
                                               chrome_options=chrome_options)

            elif platform.system() == "Windows":

                # Create driver, pass it the path to the chrome driver file and the
                #  special configurations you want to run
                self.driver = webdriver.Chrome(executable_path=os.path.
                                               join(output_path, 'chrome', 'chromedriver.exe'),
                                               chrome_options=chrome_options)
        elif browser == "Safari":
            self.driver = webdriver.Safari()

        self.driver.get(baseURL)
        self.driver.implicitly_wait(driverconfig.LONG_WAIT)

    def return_driver(self):
        return self.driver
