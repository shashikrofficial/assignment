from UtilityPackage.SeleniumDriver import SeleniumDriver
import time,json


"""
AMAZON SEARCH RESULT class : Page class which contains all required methods and variables. 
All the methods can be re-used by creating object of this class and calling as object.method()
to execute the test case.
"""


class AmazonSearchResultPage(SeleniumDriver):

    def __init__(self, driver,locator):
        #super().__init__(driver)
        self.driver = driver
        with open(locator) as f:
            data = json.load(f)
        self.locator = data

    def select_nth_result(self,item_num):
        if self.check_element_exist(item_num):
            element = self.getElement((self.locator["SELECT_Nth_RESULT"]["xpath"]).format(item_num),
                                      locatorType="xpath")
            self.highlight(element)
            self.elementClick((self.locator["SELECT_Nth_RESULT"]["xpath"]).format(item_num), locatorType="xpath")
        else:
            element = self.getElement((self.locator["SELECT_RESULT"]["xpath"]).format(item_num),
                                      locatorType="xpath")
            self.highlight(element)
            self.elementClick((self.locator["SELECT_RESULT"]["xpath"]).format(item_num), locatorType="xpath")

    def check_element_exist(self,item_num):
        return self.elementPresenceCheck((self.locator["SELECT_Nth_RESULT"]["xpath"]).format(item_num),"xpath")

    def get_search_category_name(self):
        element = self.getElement(self.locator["SEARCH_CATEGORY"]["xpath"], locatorType="xpath")
        self.highlight(element)
        return self.get_value_of_element(self.locator["SEARCH_CATEGORY"]["xpath"], locatorType="xpath")

    def get_search_text(self):
        element = self.getElement(self.locator["SEARCH_TEXT"]["xpath"], locatorType="xpath")
        self.highlight(element)
        return self.get_value_of_element(self.locator["SEARCH_TEXT"]["xpath"], locatorType="xpath")
