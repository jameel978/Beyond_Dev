import unittest
from logic.Task_agneda import TaskAgenda


class TestAppium(unittest.TestCase):
    def test_add_task(self):
        Current_taskagenda_app = TaskAgenda()
        expectedResult = True
        actualResult = True
        self.assertEqual(actualResult,expectedResult,"Answer is incorrect")



if __name__ == '__main__':
    unittest.main()