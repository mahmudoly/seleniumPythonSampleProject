import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    # Set up the WebDriver
    driver = webdriver.Chrome()  # or webdriver.Firefox() depending on your browser
    request.cls.driver = driver  # Make the driver available to the test class
    yield
    driver.quit()  # Clean up and close the driver after tests

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run the test
    outcome = yield
    report = outcome.get_result()
    with open('reports/logs.txt', 'a') as f:
        if report.when == 'call':
            f.write(f'Test: {report.nodeid}\n')
            if report.passed:
                f.write('Result: PASSED\n\n')
            else:
                f.write(f'Result: FAILED\n')
                f.write(f'        {report.longrepr}\n\n')
