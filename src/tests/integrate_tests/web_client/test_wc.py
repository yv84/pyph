# /usr/bin/python3

# python3 -m unittest -v testing.test1
import unittest

from selenium import webdriver


class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1024,768)
        self.driver.get('http://localhost:9000/')

    def tearDown(self):
        self.driver.close()

    def testIndexPage(self):
        self.assertTrue((self.driver.find_element_by_class_name("text-muted")).text == 'web_client')







if __name__ == '__main__':
    print(get_exec_path())
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner().run(suite)
    #unittest.main()
