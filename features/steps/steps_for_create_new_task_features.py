from behave import *
from pages.app_screen_for_create_new_task import CreateNewTask

use_step_matcher("re")


@given('At First Open "To Do List" App')
def step_impl(context):
    CreateNewTask(context).open_app()


@when('Click on "\+" Icon')
def step_impl(context):
    CreateNewTask(context).click_on_plus_icon_for_create_new_task()


@then("Enter Task Name In The Input Section")
def step_impl(context):
    CreateNewTask(context).input_task_name()


@then("Click On Calendar Section And Select Date")
def step_impl(context):
    CreateNewTask(context).calendar_icon_for_date()


@then('Click On "Ok" Button')
def step_impl(context):
    CreateNewTask(context).ok_button_for_save_date_and_time()


@then("Click On Time Section")
def step_impl(context):
    CreateNewTask(context).time_icon_for_time()


@then('Click On "Tick Mark" Icon')
def step_impl(context):
    CreateNewTask(context).new_task_save()


@then("Verify The task In List")
def step_impl(context):
    CreateNewTask(context).verify_task_in_list()


@then("Click On Close Task Box, It Will Closed The Task")
def step_impl(context):
    CreateNewTask(context).close_task()


@then("Verify The Task Is Closed")
def step_impl(context):
    CreateNewTask(context).closed_verify()


@then('Click On "Default DropDown" Section And Select "Personal"')
def step_impl(context):
    CreateNewTask(context).task_category_personal()


@then('Click On "Default DropDown" Section And Select "Shopping"')
def step_impl(context):
    CreateNewTask(context).task_category_shopping()


@then('Click On "Default DropDown" Section And Select "Wishlist"')
def step_impl(context):
    CreateNewTask(context).task_category_wishlist()


@then('Click On "Default DropDown" Section And Select "Work"')
def step_impl(context):
    CreateNewTask(context).task_category_work()