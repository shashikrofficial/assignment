from PageObjectsPackage.HomePageObjects import AmazonHomePage
from PageObjectsPackage.SearchResultPageObject import AmazonSearchResultPage
from PageObjectsPackage.ProductDetailsPageObject import AmazonProductDetailsPage
from ConfigVars.FrameworkConfig import urls
from ConfigVars.TestConfig import Input
import UtilityPackage.CustomLogger as cl
import logging
from UtilityPackage.DriverIntialization import DriverIntialization
import unittest
import pytest,re,os


class AmazonBooksDetails(unittest.TestCase):
    baseURL = urls.HOME_PAGE
    log = cl.customLogger(logging.DEBUG)

    @classmethod
    def setUpClass(cls):
        driver = DriverIntialization(urls.HOME_PAGE).return_driver()
        cls.driver = driver
        cls.homePageObj = AmazonHomePage(driver, 'PageObjectLocator/HomePageElementLocators.json')
        cls.searchResultPage = AmazonSearchResultPage(driver,'PageObjectLocator/SearchResultPageLocators.json')
        cls.productDetailsPage = AmazonProductDetailsPage(driver, 'PageObjectLocator/ProductDetailsPageLocators.json')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @pytest.mark.run(order=1)
    def test_browser(self):
        try:
            self.driver.get(self.baseURL)
            '''Verify the page title'''
            page_titlle=str(self.homePageObj.get_title()).lower()
            self.assertIn('amazon',page_titlle,'No Matching title')
            '''Verify the opend url'''
            self.assertIn(urls.HOME_PAGE,self.driver.current_url,'Url not matching with Input url')
        except TypeError as e:
            self.log.error("Exception occured " + str(e))



    @pytest.mark.run(order=2)
    def test_search_book(self):
        try:
            self.driver.get(self.baseURL)
            '''Verifying the page title'''
            page_titlle=str(self.homePageObj.get_title()).lower()
            self.assertIn('amazon',page_titlle,'No Matching title')

            '''Verifying the opend url'''
            self.assertIn(urls.HOME_PAGE,self.driver.current_url,'Url not matching with Input url')

            '''Verifying that CATEGORY is available in the drop down'''
            category=self.homePageObj.get_category_list()
            self.log.info(category)
            self.assertIn(Input.CATEGORY, category[0], "Category given is not available")

            self.homePageObj.select_category(Input.CATEGORY)
            self.homePageObj.search_item(Input.BOOK_NAME)

            '''Verifying that CATEGORY got selected as expected.'''
            self.assertIn(Input.CATEGORY,
                          self.searchResultPage.get_search_category_name(),"Wrong Category got selected")

            '''Verifying correct Book_name got searched or not'''
            self.assertIn(Input.BOOK_NAME, self.searchResultPage.get_search_text(), 'Wrong Book Name got searched')

        except TypeError as e:
            self.log.error("Exception occured while searching" + str(e))

    @pytest.mark.run(order=3)
    def test_select_nth_search_result(self):
        try:
            self.driver.get(self.baseURL)
            '''Verifying the page title'''
            page_titlle=str(self.homePageObj.get_title()).lower()
            self.assertIn('amazon',page_titlle,'No Matching title')

            '''Verifying the opend url'''
            self.assertIn(urls.HOME_PAGE,self.driver.current_url,'Url not matching with Input url')

            '''Verifying that CATEGORY is available in the drop down'''
            category=self.homePageObj.get_category_list()
            self.log.info(category)
            self.assertIn(Input.CATEGORY, category[0], "Category given is not available")

            self.homePageObj.select_category(Input.CATEGORY)
            self.homePageObj.search_item(Input.BOOK_NAME)

            '''Verifying that CATEGORY got selected as expected.'''
            self.assertIn(Input.CATEGORY,
                          self.searchResultPage.get_search_category_name(),"Wrong Category got selected")

            '''Verifying correct Book_name got searched or not'''
            self.assertIn(Input.BOOK_NAME, self.searchResultPage.get_search_text(), 'Wrong Book Name got searched')

            self.searchResultPage.select_nth_result(Input.ITEM_NUMBER - 1)
            '''Verifying the nth item got selected'''
            # Getting current url
            current_uri = str(self.driver.current_url)
            # Parsing current uri to extract the element number.
            uri_ref = re.search(r'ref=\w+', current_uri.replace('/', ' ')).group()
            self.assertEqual(uri_ref[-1:], str(Input.ITEM_NUMBER))

        except TypeError as e:
            self.log.error("Exception occured while searching" + str(e))

    @pytest.mark.run(order=4)
    def test_extract_all_info_of_the_product(self):
        try:
            self.driver.get(self.baseURL)
            '''Verifying the page title'''
            page_titlle = str(self.homePageObj.get_title()).lower()
            self.assertIn('amazon', page_titlle, 'No Matching title')

            '''Verifying the opend url'''
            self.assertIn(urls.HOME_PAGE, self.driver.current_url, 'Url not matching with Input url')

            '''Verifying that CATEGORY is available in the drop down'''
            category = self.homePageObj.get_category_list()
            self.log.info(category)
            self.assertIn(Input.CATEGORY, category[0], "Category given is not available")

            self.homePageObj.select_category(Input.CATEGORY)
            self.homePageObj.search_item(Input.BOOK_NAME)

            '''Verifying that CATEGORY got selected as expected.'''
            self.assertIn(Input.CATEGORY,
                          self.searchResultPage.get_search_category_name(), "Wrong Category got selected")

            '''Verifying correct Book_name got searched or not'''
            self.assertIn(Input.BOOK_NAME, self.searchResultPage.get_search_text(), 'Wrong Book Name got searched')

            self.searchResultPage.select_nth_result(Input.ITEM_NUMBER - 1)
            '''Verifying the nth item got selected'''
            # Getting current url
            current_uri = str(self.driver.current_url)
            # Parsing current uri to extract the element number.
            uri_ref = re.search(r'ref=\w+', current_uri.replace('/', ' ')).group()
            self.assertEqual(uri_ref[-1:], str(Input.ITEM_NUMBER))
            self.productDetailsPage.get_product_details(Input.OUTPUT_FILE_NAME)
            '''Verifying that output got saved successfully'''
            assert os.path.exists(Input.OUTPUT_FILE_NAME)

        except TypeError as e:
            self.log.error("Exception occured while extracting information" + str(e))
