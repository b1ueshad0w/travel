import unittest
import main

class TestUiModels(unittest.TestCase):
    def test_get_query_params(self):
        main.get_query_params()

    def test_main(self):
        main.main()
