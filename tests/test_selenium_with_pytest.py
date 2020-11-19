'''
depends on `pytest-asyncio`

Console debug:
  set PYTHONPATH = "/path/to/DevOpsDashboard/Monitor"
  pytest

idea:
  Settings(Or Preferences) -> Tools -> Python integrated tools -> testing -> default test runner -> pytest
'''

# Import the 'modules' that are required for execution for Selenium test automation
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys


@pytest.fixture(scope="class")
def firefox_driver_init(request):
    """ Fixture for Firefox """
    ''' 启动本地测试驱动 '''
    driver = webdriver.Firefox()

    ''' 连接远程测试驱动 '''
    #driver = webdriver.Remote(
    #    command_executor='http://127.0.0.1:4444/wd/hub',
    #    desired_capabilities=DesiredCapabilities.FIREFOX
    #)

    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    """ Fixture for Chrome """
    driver = webdriver.Chrome()

    ''' 连接远程测试驱动 '''
    #driver = webdriver.Remote(
    #    command_executor='http://127.0.0.1:4444/wd/hub',
    #    desired_capabilities=DesiredCapabilities.CHROME
    #)

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.usefixtures("firefox_driver_init")
class BasicFirefoxTest:
    pass


class TestURL(BasicFirefoxTest):
    def test_open_url(self):
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()

        title = "Google"
        assert title == self.driver.title

        search_text = "wangji.pro"
        ''' 通过 xpath 查找 html 组件 '''
        search_box = self.driver.find_element_by_xpath("//input[@name='q']")
        search_box.send_keys(search_text)

        time.sleep(2)

        ''' 动作 '''
        # Option 1 - To Submit the search
        # search_box.submit()

        # Option 2 - To Submit the search
        search_box.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        search_box.send_keys(Keys.ARROW_UP)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)

        time.sleep(5)

        # Click on the LambdaTest HomePage Link
        title = "你需要知道的有关泛函编程一些知识 —— effect 和 side effect - 直到世界的尽头"
        lt_link = self.driver.find_element_by_xpath("//h3[.='你需要知道的有关泛函编程一些知识—— effect 和side effect - zio']")
        lt_link.click()

        time.sleep(5)
        ''' 断言 '''
        assert title == self.driver.title
        time.sleep(2)


@pytest.mark.usefixtures("chrome_driver_init")
class BasicChromeTest:
    pass


class TestURLChrome(BasicChromeTest):
    def test_open_url(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()

        self.driver.find_element_by_name("li1").click()
        self.driver.find_element_by_name("li2").click()

        title = "Sample page - lambdatest.com"
        assert title == self.driver.title

        sample_text = "Happy Testing at LambdaTest"
        email_text_field = self.driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)
        time.sleep(5)

        self.driver.find_element_by_id("addbutton").click()
        time.sleep(5)

        output_str = self.driver.find_element_by_name("li6").text
        sys.stderr.write(output_str)

        time.sleep(2)
