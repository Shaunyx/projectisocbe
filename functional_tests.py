from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_in_home_page_title(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('Home', self.browser.title)


        # She is invited to enter a to-do item straight away

    def test_login_in_login_page(self):

        self.browser.get('http://localhost:8000/accounts/login/')
        self.assertIn('Login', self.browser.title)



# creer page a propos
    def test_page_a_propos(self):

        self.browser.get('http://localhost:8000/pages/a-propos')
        self.assertIn('A propos', self.browser.title)

# creer page isoc dans le monde
    def test_page_isoc_dans_le_monde(self):

        self.browser.get('http://localhost:8000/pages/isoc-dans-le-monde')
        self.assertIn('Isoc dans le monde', self.browser.title)

# creer page notre mission
    def test_page_notre_mission(self):
        self.browser.get('http://localhost:8000/pages/notre-mission')
        self.assertIn('Notre mission', self.browser.title)


# verifier losrque l'utilisateur est sur la page d'accueil si il clic le bouton mission il arrive sur la page mission

    def test_mission_button_clique(self):
         self.browser.get('http://localhost:8000')
         result = self.browser.find_element_by_css_selector("a.mission")
         result.click()
         self.assertIn('Notre mission', self.browser.title)



# verifier lorsque l'utilisateur clique sur le bouton à propos soit rediriger vers la page à propos

    def test_a_propos_button_clique(self):
         self.browser.get('http://localhost:8000')
         result = self.browser.find_element_by_css_selector("a.a_propos")
         result.click()
         self.assertIn('A propos', self.browser.title)


         self.fail('Finish the test!')
if __name__ == '__main__':
     unittest.main(warnings='ignore')
