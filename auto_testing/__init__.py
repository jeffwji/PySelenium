from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def __test():
    ''' 启动本地测试驱动 '''
    driver = webdriver.Firefox()

    ''' 连接远程测试驱动 '''
    #driver = webdriver.Remote(
    #    command_executor='http://127.0.0.1:4444/wd/hub',
    #    desired_capabilities=DesiredCapabilities.FIREFOX
    #)
    driver.get("http://www.python.org")

    assert "Python" in driver.title

    ''' 通过 element name 查找 html 组件 '''
    elem = driver.find_element_by_name("q")

    ''' 动作 '''
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

    ''' 断言 '''
    assert "No results found." not in driver.page_source
    
    ''' 关闭驱动 '''
    driver.close()


if __name__ == '__main__':
    __test()
