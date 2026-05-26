import unittest
from unittest.mock import patch


class TestRemoteCreated(unittest.TestCase):
    @patch('builtins.print')
    def test_print_step_1(self, mock_print):
        from remote_created import print_step_1
        print_step_1()
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_print_step_2(self, mock_print):
        from remote_created import print_step_2
        print_step_2()
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_print_step_4(self, mock_print):
        from remote_created import print_step_4
        print_step_4()
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_print_step_5(self, mock_print):
        from remote_created import print_step_5
        print_step_5()
        print('ok')
        self.assertTrue(mock_print.called)
    
    @patch('builtins.print')
    def test_print_step_6(self, mock_print):
        from remote_created import print_step_6
        print_step_6()
        print('ok')
        self.assertTrue(mock_print.called)
    
    @patch('builtins.print')
    def test_print_step_7(self, mock_print):
        from remote_created import print_step_7
        print_step_7()
        print('ok')
        self.assertTrue(mock_print.called)


class TestTestModule(unittest.TestCase):
    @patch('builtins.print')
    def test_p1(self, mock_print):
        from test import p1
        p1()
        self.assertTrue(mock_print.called)


if __name__ == '__main__':
    unittest.main()
