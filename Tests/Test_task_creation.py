import unittest
from Logic.Task_agneda_homepage import TaskAgenda
from datetime import datetime, timedelta



class Test_task_agenda_task_creation(unittest.TestCase):
    
    def setUp(self):
        self.Current_taskagenda_app = TaskAgenda()
        self.Current_taskagenda_app.create_new_task_from_homepage_using_add_sign("beyond_dev",day='Today')

    def test_adding_a_task(self):
        Result = self.Current_taskagenda_app.check_if_event_is_added()
        self.assertTrue(Result,"EVENT FAILED TO ADD")

    def test_added_task_name(self):
        Result = self.Current_taskagenda_app.get_current_event_name()
        self.assertEqual(Result,"beyond_dev","EVENT NAME IS NOT CORRECT")

    def test_added_task_date_today(self):
        Result = self.Current_taskagenda_app.get_current_event_date()
        Expected_result = datetime.now().strftime('%d %h %Y')
        self.assertEqual(Result,Expected_result,"EVENT DATE IS NOT CORRECT")
        
    def test_deleting_an_event(self):
        self.Current_taskagenda_app.delete_added_event()
        Result = self.Current_taskagenda_app.check_if_event_is_added()
        self.assertFalse(Result,"EVENT WAS NOT DELETED")

    def test_mark_task_as_completed(self):
        self.Current_taskagenda_app.mark_event_as_complete()
        Result = self.Current_taskagenda_app.check_if_event_is_complete()
        Expected_result = "true"
        self.assertEqual(Result, Expected_result, "EVENT IS NOT MARKED AS COMPLETE")
        
if __name__ == '__main__':
    unittest.main()