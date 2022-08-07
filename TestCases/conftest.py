import pytest
from appium import webdriver
import allure
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def appium_driver(request):
    desire_cap = {}
    desire_cap['deviceName'] = 'emulator-5554'
    desire_cap['platformName'] = 'Android'
    desire_cap['appPackage'] = "com.goibibo"
    desire_cap['appActivity'] = "com.goibibo.common.HomeActivity"
    desire_cap['noReset'] = True
    # desire_cap['app'] = 'C:\\Users\\dines\\Downloads\\flipboard.apk'
    driver = webdriver.Remote("127.0.0.1:4723/wd/hub", desire_cap)
    request.cls.driver = driver
    driver.implicitly_wait(20)

    yield driver
    driver.quit()

@pytest.fixture()
def log_on_faliure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)