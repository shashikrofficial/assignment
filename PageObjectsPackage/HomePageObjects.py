from UtilityPackage.SeleniumDriver import SeleniumDriver
import time,json


"""
AMAZON HOME_PAGE class : Page class which contains all required methods and variables. 
All the methods can be re-used by creating object of this class and calling as object.method()
to execute the test case.
"""


class AmazonHomePage(SeleniumDriver):

    def __init__(self, driver,locator):
        #super().__init__(driver)
        self.driver = driver
        with open(locator) as f:
            data = json.load(f)
        self.locator = data

    def select_category(self, category):
        element=self.getElement(self.locator["SEARCH_DROP_DOWN"]["xpath"],locatorType="xpath")
        self.highlight(element)
        self.select_visible_text(self.locator["SEARCH_DROP_DOWN"]["xpath"], "xpath",category)

    def search_item(self,item_name):
        self.highlight(self.getElement(self.locator["SEARCH_BOX"]["id"],locatorType="id"))
        self.sendKeys(item_name,self.locator["SEARCH_BOX"]["id"],locatorType="id")
        self.highlight(self.getElement(self.locator["SEARCH_BUTTON"]["xpath"],locatorType="xpath"))
        self.elementClick(self.locator["SEARCH_BUTTON"]["xpath"],locatorType="xpath")

    def get_title(self):
        return self.getTitle()

    def get_category_list(self):
        category_list=self.getElements(self.locator["SEARCH_DROP_DOWN"]["xpath"],locatorType="xpath")
        list_cat=[]
        for category in category_list:
            list_cat.append(category.text)
        return list_cat
