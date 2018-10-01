from behave import *
from features.pages.Assignment3_page import Keyword


@step("Go to the {section_name}")
def step_impl(context, section_name):
    Keyword(context.driver).keyword_identifier(section_name)


@when("Navigate to the stride website")
def step_impl(context):
    Keyword(context.driver).navigate_to_website()


@step("Click on load random text")
def step_impl(context):
    Keyword(context.driver).random_text()


@step("Save random text")
def step_impl(context):
    Keyword(context.driver).save_random_text1()


@step("Click on analyze section")
def step_impl(context):
    Keyword(context.driver).analyze_section()


@step("Choose compression ratio")
def step_impl(context):
    Keyword(context.driver).compression_ratio()


@step("Enter the text")
def step_impl(context):
    Keyword(context.driver).identifier_text()


@step("Enter the text in summarization section")
def step_impl(context):
    Keyword(context.driver).summarization_text()


@step("Enter the text in sentiment analysis")
def step_impl(context):
    Keyword(context.driver).sentiment_analysis_text()


@step("Select the language")
def step_impl(context):
    Keyword(context.driver).language()


@when("Go to the {setting} page")
def step_impl(context, setting):
    Keyword(context.driver).click_on_settings(setting)


@step("I see the home page")
def step_impl(context):
    Keyword(context.driver).home_page()


@step("I see the about page")
def step_impl(context):
    Keyword(context.driver).about_page()


@step("I see the technology page")
def step_impl(context):
    Keyword(context.driver).technology_page()


@step("I see the solution page")
def step_impl(context):
    Keyword(context.driver).solution_page()


@step("I see the team page")
def step_impl(context):
    Keyword(context.driver).team_page()


@step("I enter the full name")
def step_impl(context):
    Keyword(context.driver).full_name()


@step("I enter the email id")
def step_impl(context):
    Keyword(context.driver).email()


@step("I enter the phone number")
def step_impl(context):
    Keyword(context.driver).phone_number()


@step("I enter the text message")
def step_impl(context):
    Keyword(context.driver).enter_text()


@step("Save the detail")
def step_impl(context):
    Keyword(context.driver).save_detail()


@step("Close the contact section")
def step_impl(context):
    Keyword(context.driver).close_contact_section()


@when("I go to contact page")
def step_impl(context):
    pass
