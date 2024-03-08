import unittest
from Logic.Task_agneda_homepage import TaskAgenda
from datetime import datetime, timedelta



class Test_task_agenda_task_dates(unittest.TestCase):
    
    def setUp(self):
        self.Current_taskagenda_app = TaskAgenda()
        
    def test_add_task_with_empty_name(self):
        self.Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("",day='Today')
        Result = self.Current_taskagenda_app.check_if_event_is_added()
        self.assertFalse(Result,"EVENT WAS ADDED")

    def test_added_task_date_tomorrow(self):
        self.Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("beyond_dev",day='Tomorrow')
        Result = self.Current_taskagenda_app.get_current_event_date_from_hamburger_menu()
        Expected_result = (datetime.now()+timedelta(days=1)).strftime('%d %h %Y')
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")

    def test_added_task_date_customdate(self):
        self.Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("beyond_dev",day='Other')
        self.Current_taskagenda_app.select_date_from_month_stock_view_finder('1 Jan 2025')
        self.Current_taskagenda_app.add_name_to_task("Next Year TASK")
        Result = self.Current_taskagenda_app.get_current_event_date_from_hamburger_menu()
        Expected_result = "1 Jan 2025"
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")

    def test_adding_a_task_from_calendar_tab(self):
        self.Current_taskagenda_app.create_new_task_from_homepage_using_calendar_tab("Beyond Dev",date='4 Jan 2025')
        Result = self.Current_taskagenda_app.get_current_event_date()
        Expected_result = "4 Jan 2025"
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")



if __name__ == '__main__':
    unittest.main()