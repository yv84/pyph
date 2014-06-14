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

        self.assertTrue(len(self.driver.find_elements_by_css_selector(".dropdown.btn-group.gsconnection")) == 1)
        self.assertTrue((self.driver.find_elements_by_css_selector(".dropdown.btn-group.gsconnection"))[0].text == 'GSConnection: Conn1')

        self.assertTrue(self.driver.find_element_by_css_selector("#btn-connect").text == 'Connect')
        self.assertTrue(self.driver.find_element_by_css_selector("#btn-stop").text == 'Stop')
        self.assertTrue(self.driver.find_element_by_css_selector("#btn-clear").text == 'Clear')
        self.assertTrue(self.driver.find_element_by_css_selector("#status").text == 'disconnected')

        self.assertTrue(len(self.driver.find_elements_by_css_selector(".span1.packet_log")) == 1) # #log
        self.assertTrue(len(self.driver.find_elements_by_css_selector(".span1.packet_log")) == 1)
        self.assertTrue(self.driver.find_element_by_css_selector(".span1.packet_log > dt").text == 'log')
        self.assertTrue(len(self.driver.find_elements_by_css_selector(".span1.packet_log > dd")) > 0)





if __name__ == '__main__':
    print(get_exec_path())
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner().run(suite)
    #unittest.main()
