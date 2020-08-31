from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class JeffTest(unittest.TestCase):

    def setUp(self):
        #Jeff is looking for a blog written by Elmaan 
        self.driver = webdriver.Firefox(executable_path=r'/Users/elmaanshikder/Downloads/geckodriver')
        
    
    def tearDown(self):
        #he is done with the internet for today
        self.driver.quit()

    def test_navigate_to_cv_editor(self):
        self.driver.get('http://127.0.0.1:8000')
        #He notices that the title is is the name of the person he is looking for
        assert 'Elmaan Blog' in self.driver.title , "instead title is " + self.driver.title

        #jeff is warmly invited to read the blog
        assert 'Welcome to my blog' in self.driver.find_element_by_tag_name('h1').text

        #he notices that there is a link to Elmaan's cv and navigates to the next page where he is welcomed
        self.driver.get('http://127.0.0.1:8000/cv')
        assert 'here is my cv' in self.driver.find_element_by_tag_name('p').text ,"found "+ self.driver.find_element_by_tag_name('p').text

        #Jeff having employed Elmaan in the past wants to add that employment history to his cv, and so navigates to the editor page where he can add elements to the cv
        self.driver.get('http://127.0.0.1:8000/editor')
        ainputbox = self.driver.find_element_by_id('add_education')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'update education'
        )
        #He enters the details inside the box and hits enter
        inputbox.send_keys('worked for 3 months at summer camp, in 2018, great guy')
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(10)

        #Jeff then goes back to the cv to see if his input has been updated
        self.driver.get('http://127.0.0.1:8000/cv')
        section = self.driver.find_element_by_id('education')
        parts = table.find_elements_by_tag_name('p')
        self.assertTrue(
            any(row.text == 'worked for 3 months at summer camp, in 2018, great guy' for part in parts)
        )

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 
        
    