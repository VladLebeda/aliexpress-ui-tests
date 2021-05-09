Introduction
------------

# aliexpress-ui-tests

Test task for autotesting  Aliexpress shop UI (best.aliexpress.com). 

Python, Pytest, Selenium. TODO: Allure, Jenkins/Circleci.

Result so far
------------
![image](https://user-images.githubusercontent.com/59774558/117587686-cd3b7980-b127-11eb-826a-8488f1da53f1.png)






How To Run
----------------

1) Install requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```

Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.





