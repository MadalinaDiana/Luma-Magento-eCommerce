<span style="color: orange"> # Luma-Magento-eCommerce </span>
Final Project ItFactory-Selenium
## Gherkin project
This project tests multiple types of pages, in chrome. The POM structure is used for a better organization of the files.
## Scnerio Outline 
This project use multiple scenario outline that make basically replaces variable/keywords with the value from the table. Each row in the table is considered to be a scenario.
## Hooks
Hooks (event bindings) can be used to perform additional automation logic at specific times, such as any setup required prior to executing a scenario. In order to use hooks, you need to add the Binding attribute to your class.
    ### [BeforeScenario] or [Before]
        [AfterScenario] or [After] (that I used when initializing the browser) -> Automation logic that has to run before/after executing each scenario or scenario outline example.

## To clone this project use the simple steps below
Go to the top of the Github project -> Above the list of files and folders, click Code ->Copy the URL of the project - Open Terminal in Pycharm - Change the current location to the directory where you want to attach the project - Type git clone and paste the copied url - Press enter. 
<p align="center" style="color: green">  <b>Or</b> </p>

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
        /base_page.py  #here we have some important functions defined
        /begin_home_page.py
        /create_account.py
        /enter_sign_in.py
        /functionality_account.py
    /steps #here we implement steps to be executed,
            # using the methods defined in pages
        /begin_home_page.py
        /create_account.py
        /enter_sign_in.py
        /functionality_account.py
    /browser.py #here is where test execution is initialized
    /begin_home_page.feature #here are the tests in Gherkin language
    /create_account.feature 
    /enter_sign_in.feature
    /functionality_account.feature
    /environment.py #here we set hooks that put the browser in context
/behave.ini #here we initialize the creation of the html report
```
## About the testing HomePage
In this feature 61 steps and 14 scenarios were executed and tested, more precisely the following were tested:

1. Search with empty/valid input.
2. Navbar buttons redirect correctly.
3. Functionality of first product details.
4. Invalid/valid input for subscription.

## About the testing Create Acoount
In this feature 14 steps and 4 scenarios were executed and tested, more precisely the following were tested:
    
1. Invalid/Valid input data.

## About the testing Verify Sign In
In this feature 11 steps and 3 scenarios were executed and tested, more precisely the following were tested:

1. Verify the buttons.
2. Sign in account.

## About the testing Account functionality
In this feature 50 steps and 6 scenarios were executed and tested, more precisely the following were tested:

1. Buy items.
2. Write review.
3. Compare products
4. Update My Wish List

After running the code with html report creation after, we will have the following report:
    <img width="1439" alt="image" src="https://user-images.githubusercontent.com/48148610/207374230-864e5c14-1ad9-4653-98a6-e225307a3bc1.png">
In this report we will see steps and scenarios that are successfully executed. Steps marked as "Passed" belong to the background passed in scenarios. It is run before the scenario, and without it scenarios cannot be executed successfully. It can be referred to as a prerequisite. 
    
    

