import unittest
from logic.Task_agneda import TaskAgenda
from datetime import datetime, timedelta



class TestAppium(unittest.TestCase):
    def test_add_task_with_empty_name(self):
        Current_taskagenda_app = TaskAgenda()
        Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("",day='Today')
        Current_taskagenda_app.click_save_button()
        Result = Current_taskagenda_app.check_if_event_is_added()
        self.assertFalse(Result,"EVENT WAS ADDED")

    def test_adding_a_task(self):
        Current_taskagenda_app = TaskAgenda()
        Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("beyond_dev",day='Today')
        Current_taskagenda_app.click_save_button()
        Result = Current_taskagenda_app.check_if_event_is_added()
        self.assertTrue(Result,"EVENT FAILED TO ADD")

    def test_added_task_name(self):
        Current_taskagenda_app = TaskAgenda()
        Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("beyond_dev",day='Today')
        Current_taskagenda_app.click_save_button()
        Result = Current_taskagenda_app.get_current_event_name()
        Expected_result = "beyond_dev"
        self.assertEqual(Result,Expected_result,"EVENT NAME IS NOT CORRECT")

    def test_added_task_date_today(self):
        Current_taskagenda_app = TaskAgenda()
        Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("beyond_dev",day='Today')
        Current_taskagenda_app.click_save_button()
        Result = Current_taskagenda_app.get_current_event_date()
        Expected_result = datetime.now().strftime('%d %h %Y')
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")

    def test_added_task_date_tomorrow(self):
        Current_taskagenda_app = TaskAgenda()
        Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("beyond_dev",day='Tomorrow')
        Current_taskagenda_app.click_save_button()
        Result = Current_taskagenda_app.get_current_event_date()
        Expected_result = (datetime.now()+timedelta(days=1)).strftime('%d %h %Y')
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")

    def test_added_task_date_custom_data(self):
        Current_taskagenda_app = TaskAgenda()
        Current_taskagenda_app.select_date_from_month_stock_view_finder("beyond_dev",day='Other')
        Current_taskagenda_app.select_date_from_month_view_finder('1 Jan 2025')
        Current_taskagenda_app.add_name_to_task("Next Year TASK")
        Current_taskagenda_app.click_save_button()
        Result = Current_taskagenda_app.get_current_event_date()
        Expected_result = "1 Jan 2025"
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")

    def test_added_task_date_custom_data(self):
        Current_taskagenda_app = TaskAgenda()
        Current_taskagenda_app.create_new_task_from_homepage_using_calendar_tab("Next Year TASK",'1 Jan 2025')
        Current_taskagenda_app.click_save_button()
        Current_taskagenda_app.navigate_back()
        Result = Current_taskagenda_app.get_current_event_date_from_hamburger_menu()
        Expected_result = "1 Jan 2025"
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")


if __name__ == '__main__':
    unittest.main()