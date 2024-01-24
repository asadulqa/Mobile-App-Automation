from locators import app_locator
from pages.base_driver import BaseDriver

class CreateNewTask(BaseDriver):

    def open_app(self):
        pass

    def click_on_plus_icon_for_create_new_task(self):
        self.click(app_locator.add_task_id)

    def input_task_name(self):
        self.wait_for_element(app_locator.task_name_input_id, 10)
        input_field = self.driver.find_element(*self._formatter(app_locator.task_name_input_id))
        input_field.send_keys("Test Task")

    def calendar_icon_for_date(self):
        self.click(app_locator.calendar_icon_id)

    def ok_button_for_save_date_and_time(self):
        self.click(app_locator.inside_calendar_ok_button_x)

    def time_icon_for_time(self):
        self.click(app_locator.time_icon_x)

    def new_task_save(self):
        self.click(app_locator.save_tick_mark_icon_task_id)

    def verify_task_in_list(self):
        self.wait_for_element(app_locator.new_created_task_x, 10)
        verify_text = self.driver.find_element(*self._formatter(app_locator.new_created_task_x)).text
        assert verify_text == "Test Task"

    def close_task(self):
        self.wait_for_element(app_locator.close_task_id, 10)
        self.click(app_locator.close_task_id)

    def closed_verify(self):
        self.wait_for_element(app_locator.empty_list_id, 10)
        empty_text = self.driver.find_element(*self._formatter(app_locator.empty_list_id)).text
        assert empty_text == "Nothing to do"
        print("Task Closed Done!")

    def task_category_personal(self):
        self.click(app_locator.in_the_task_c_drop_down_id)
        self.click(app_locator.personal_x)

    def task_category_shopping(self):
        self.click(app_locator.in_the_task_c_drop_down_id)
        self.click(app_locator.shopping_x)

    def task_category_wishlist(self):
        self.click(app_locator.in_the_task_c_drop_down_id)
        self.click(app_locator.wishlist_x)

    def task_category_work(self):
        self.click(app_locator.in_the_task_c_drop_down_id)
        self.click(app_locator.work_x)
