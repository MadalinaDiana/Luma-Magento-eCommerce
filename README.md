# Luma-Magento-eCommerce
Final Project ItFactory-Selenium
## Gerkin project
This project tests multiple types of pages, in chrome. The POM structure is used for a better organization of the files.
## Create project
Create new project in PyCharm, with virtualenv allocated.

### Pre-requisites
Install with pip install <library name>
- behave
- behave-html-formatter
- selenium
- webdriver-manager
- Everything needed to run the project can be found in the file ```.requirements.txt```
## Folder and file structure
```bash
/features
    /pages # here we have defined the methods used
              # in the testing steps
        /base_page.py
        /home_page.py
        /create_account.py

    /steps #here we implement steps to be executed,
            # using the methods defined in pages
        /home_page.py
        /create_account.py
        
    /browser.py #here is where test execution is initialized
    /home_page.feature #here are the tests in Gherkin language
    /create_account.feature #here are the tests in Gherkin language
    /environment.py #here we set hooks that put the browser in context
/behave.ini #here we initialize the creation of the html report
```
## About the testing HomePage
In this feature 61 steps and 14 scenarios were executed and tested, more precisely the following were tested:

1. Search with empty/valid input.
2. Navbar buttons redirect correctly.
3. Functionality of first product details.
4. Invalid/valid input for subscription.

<u>For tests with multiple values, I used Scenario outline.</u>
