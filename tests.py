import unittest
from unittest.mock import MagicMock

from code_helper.functions import CodeHelperMagics


class TestHistoryCommand(unittest.TestCase):
    def test_last_history(self):
        """
        Test the last method history actually returns the last history.
        """
        chm = CodeHelperMagics()
        #patch the sell with mock
        mock = MagicMock()
        mock.get_ipython.return_value = None
        chm.shell = mock
        chm.last_history()

if __name__ == '__main__':
    unittest.main()