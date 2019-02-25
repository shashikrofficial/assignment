from UtilityPackage.SeleniumDriver import SeleniumDriver
import time,json


"""
AMAZON Product Details class : Page class which contains all required methods and variables. 
All the methods can be re-used by creating object of this class and calling as object.method()
to execute the test case.
"""


class AmazonProductDetailsPage(SeleniumDriver):

    def __init__(self, driver,locator):
        #super().__init__(driver)
        self.driver = driver
        with open(locator) as f:
            data = json.load(f)
        self.locator = data

    def get_title_of_book(self):
        element=self.getElement(self.locator["BOOK_TITLE"]["id"],locatorType="id")
        self.highlight(element)
        book_title=self.get_value_of_element(self.locator["BOOK_TITLE"]["id"],locatorType="id")
        return book_title

    def get_kindle_cost(self):
        element = self.getElement(self.locator["KINDLE_COST"]["id"], locatorType="id")
        self.highlight(element)
        kindle_cost = self.get_value_of_element(self.locator["KINDLE_COST"]["id"], locatorType="id")
        return kindle_cost

    def get_paperback_cost(self):
        element = self.getElement(self.locator["PAPERBACK_COST"]["id"], locatorType="id")
        self.highlight(element)
        paperback_cost = self.get_value_of_element(self.locator["PAPERBACK_COST"]["id"], locatorType="id")
        return paperback_cost

    def get_product_details_element(self):
        element = self.getElement(self.locator["PRODUCT_DETAILS"]["xpath"], locatorType="xpath")
        self.highlight(element)
        return element

    def get_product_details(self,outputFileName):
        elements=self.getElements(self.locator["DETAILS"]["xpath"], locatorType="xpath")
        with open(outputFileName, 'w') as fp:
            fp.write('Details of the book are as follows ::\n')
            fp.write("Book Title: "+self.get_title_of_book()+"\n")
            fp.write((self.get_kindle_cost()).replace("\n",":",1)+"\n")
            fp.write((self.get_paperback_cost()).replace("\n",":",1)+"\n")
            for item in elements:
                fp.write(item.text)
                fp.write("\n")



