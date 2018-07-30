import self as self
from behave import when, given, then, step
from behave.runner import Context
from selenium.common.exceptions import NoSuchElementException, JavascriptException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options

@given(u'we on page "{page}"')
def step_impl(context, page):
    #page = "http://www.wave-access.com/"
    # context.driver.get(page)
        context.driver.get('http://wasite:wasite@wasiteen.wavea.cc/')


@when(u'we click at button "{button}"')
def step_impl(context, button):
    context.driver.find_element_by_xpath(f'//a[contains(text(),"{button}")]').click()
    #context.driver.find_element_by_css_selector('a[href*=\'button\'][class=\'skrollable skrollable-between\']').click()
#http://www.wave-access.com/public_en/contacts.aspx


@then(u'I should see the transition to "{sections}"')
def step_impl(context, sections):
    url = context.driver.current_url
    if url == context:
        True


@when(u'we click at button phone call with id "{button}"')
def step_impl(context, button):
     context.driver.find_element_by_xpath(f'//*[@id="orderCallLink"]').click()


@when('we write "{text}" at element with id "{id}"')
def verify_title(context, text, id):
    context.driver.find_element_by_id(id).send_keys(text)


@when(u'we write "" at element with id "{id}"')
def step_impl(context, id):
    pass


@when('we click at cell checkmark')
def verify_title(context):
    try:
        context.driver.find_element_by_xpath('//div[@id="formGetStartedBox"]//input[@name="AgreePrivacyPolicy"]/parent::node()/span[@class="checkmark"]').click()
    except ElementNotVisibleException:
        context.driver.find_element_by_class_name("checkmark").click()


@when('we click at button submit')
def verify_title(context):
    try:
        context.driver.find_element_by_id('sendCallOrder').click()
    except ElementNotVisibleException:
        context.driver.find_element_by_id('getStartedSubmit').click()


@then('I should see field with id "{id}" and placeholder message "{error}"')
def step_impl(context, id, error):
    # b = context.driver.find_element_by_xpath('//div[contains(@class, \'alert-success\')]')
    # assert message in b.text
    #context.driver.find_element_by_placeholder(message)
    #context.driver.find_element_by_id('TelephoneOrderCall')
    context.driver.find_element_by_xpath(f'//input[@id="{id}"][@placeholder="{error}"]')


@when('in section "{products}" we click at button details')
def verify_title(context, products):
    elements = context.driver.find_elements_by_css_selector('h3.h3-wa.textUnder')
    for item in elements:
        if item.text == products:
            item.parent.find_element_by_xpath('//a[@class="gradientBtn"][//*[@href]]').click()
            break


    #context.driver.find_element_by_css_selector('div.visible-lg > a.gradientBtn > span.text').click()
    #context.driver.find_element_by_xpath('//div[@class="leftPart"][//*[@href]]').click()
    # context.driver.find_element_by_xpath('//a[@class="gradientBtn"][//*[@href]]').click()
    #context.driver.find_element_by_xpath('//a[@class="gradientBtn"]').click()
    #context.driver.find_element_by_xpath('//a[span[text()[contains(., \'DETAils\')]]] ')


@when('we click at button Get started')
def verify_title(context):
        context.driver.find_element_by_id('getStartedLink').click()


@then('I should see message "{success}" at element with id "{id}"')
def step_impl(context, success, id):
    context.driver.find_element_by_xpath(f'//div[@id="{id}"]/div[contains(text(),"{success}")]')
