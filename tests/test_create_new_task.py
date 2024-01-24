from pages.app_screen_for_create_new_task import CreateNewTask


def test_default_task(driver):
    todo = CreateNewTask(driver)
    todo.open_app()
    todo.click_on_plus_icon_for_create_new_task()
    todo.input_task_name()
    todo.calendar_icon_for_date()
    todo.ok_button_for_save_date_and_time()
    todo.time_icon_for_time()
    todo.ok_button_for_save_date_and_time()
    todo.new_task_save()
    todo.verify_task_in_list()
    todo.close_task()
    todo.closed_verify()


def test_personal_task(driver):
    todo = CreateNewTask(driver)
    todo.open_app()
    todo.click_on_plus_icon_for_create_new_task()
    todo.input_task_name()
    todo.calendar_icon_for_date()
    todo.ok_button_for_save_date_and_time()
    todo.time_icon_for_time()
    todo.ok_button_for_save_date_and_time()
    todo.task_category_personal()
    todo.new_task_save()
    todo.verify_task_in_list()
    todo.close_task()
    todo.closed_verify()


def test_shopping_task(driver):
    todo = CreateNewTask(driver)
    todo.open_app()
    todo.click_on_plus_icon_for_create_new_task()
    todo.input_task_name()
    todo.calendar_icon_for_date()
    todo.ok_button_for_save_date_and_time()
    todo.time_icon_for_time()
    todo.ok_button_for_save_date_and_time()
    todo.task_category_shopping()
    todo.new_task_save()
    todo.verify_task_in_list()
    todo.close_task()
    todo.closed_verify()


def test_wishlist_task(driver):
    todo = CreateNewTask(driver)
    todo.open_app()
    todo.click_on_plus_icon_for_create_new_task()
    todo.input_task_name()
    todo.calendar_icon_for_date()
    todo.ok_button_for_save_date_and_time()
    todo.time_icon_for_time()
    todo.ok_button_for_save_date_and_time()
    todo.task_category_wishlist()
    todo.new_task_save()
    todo.verify_task_in_list()
    todo.close_task()
    todo.closed_verify()


def test_work_task(driver):
    todo = CreateNewTask(driver)
    todo.open_app()
    todo.click_on_plus_icon_for_create_new_task()
    todo.input_task_name()
    todo.calendar_icon_for_date()
    todo.ok_button_for_save_date_and_time()
    todo.time_icon_for_time()
    todo.ok_button_for_save_date_and_time()
    todo.task_category_work()
    todo.new_task_save()
    todo.verify_task_in_list()
    todo.close_task()
    todo.closed_verify()
