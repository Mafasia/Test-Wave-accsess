from selenium.webdriver.support.ui import WebDriverWait
import csv
from selenium.webdriver.support import expected_conditions as ec
from behave import when, given, then
from selenium.common.exceptions import ElementNotVisibleException

CRED = "wasite:wasite"


def normalize_url(url: str) -> str:
    return url.replace(f"{CRED}@", "")


@given(u'we on page "test site"')
def step_page(context):
    context.driver.get(f'http://{CRED}@wasiteen.wavea.cc/')
    context.driver.maximize_window()


@when(u'we click at sections and we should see correct url')
def step_click(context):

    def csv_dict_reader(file_obj):
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            context.driver.find_element_by_xpath(
                f'//a[contains(text(),"{(line["section"])}")]').click()
            url = context.driver.current_url
            need_url = f'http://{CRED}@wasiteen.wavea.cc/public_en' \
                       f'/{(line["sections"])}.aspx'
            assert url == need_url

    with open("resources/menu.csv") as f_obj:
        csv_dict_reader(f_obj)


@when(u'we click at button "{button}"')
def step_button(context, button):
    context.driver.find_element_by_xpath(
        f'//a[contains(text(),"{button}")]').click()


@then('in section "{products}" we click at button details '
      'and we should see the transition to "{sections}"')
def step_details(context, products, sections):
    wait = WebDriverWait(context.driver, 5)

    context.current_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles

    context.driver.find_element_by_xpath(
        f'//h3[@class="h3-wa textUnder" and contains(text(),'
        f' "{products}")]/parent::node()//a').click()
    wait.until(ec.new_window_is_opened(context.old_windows))

    new_window = [i for i in context.driver.window_handles
                  if i not in context.old_windows]
    context.driver.switch_to.window(new_window[0])

    url = context.driver.current_url

    context.driver.close()
    context.driver.switch_to.window(context.current_window)

    assert normalize_url(url) == sections


@when(u'we click at button phone call with id "{button}"')
def step_phone(context, button):
    context.driver.find_element_by_xpath(f'//*[@id="orderCallLink"]').click()


@when('we write "{text}" at element with id "{id}"')
def step_text(context, text, id):
    context.driver.find_element_by_id(id).send_keys(text)


@when(u'we write "" at element with id "{id}"')
def step_empty(context, id):
    pass


@when('we click at cell checkmark')
def step_check(context):
    try:
        context.driver.find_element_by_xpath(
            '//div[@id="formGetStartedBox"]//input[@name="AgreePrivacyPolicy"]'
            '/parent::node()/span[@class="checkmark"]'
        ).click()
    except ElementNotVisibleException:
        context.driver.find_element_by_class_name("checkmark").click()


@when('we click at button submit')
def step_click(context):
    try:
        context.driver.find_element_by_id('sendCallOrder').click()
    except ElementNotVisibleException:
        context.driver.find_element_by_id('getStartedSubmit').click()


@then('I should see field with id "{id}" and placeholder message "{error}"')
def step_msg(context, id, error):
    context.driver.find_element_by_xpath(f'//input[@id="{id}"]'
                                         f'[@placeholder="{error}"]')


@when('we click at button Get started')
def step_start(context):
    context.driver.find_element_by_id('getStartedLink').click()


@then('I should see message "{success}" at element with id "{id}"')
def step_scs(context, success, id):
    context.driver.find_element_by_xpath(
        f'//div[@id="{id}"]/div[contains(text(),"{success}")]')
