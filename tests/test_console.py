#!/usr/bin/python3
"""Tests HBNBCommand commands in console module"""

import unittest
from unittest.mock import patch
from io import StringIO
from models import *
from console import HBNBCommand


class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        self.console.onecmd("create BaseModel")
        id = mock_stdout.getvalue().strip()
        self.assertTrue(len(id) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_createFail(self, mock_stdout):
        self.console.onecmd("create state")
        output = mock_stdout.getvalue()
        self.assertIn("class doesn't exists",  output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_parameter(self, mock_stdout):
        self.console.onecmd('create State name="California"')
        id = mock_stdout.getvalue().strip()
        self.assertTrue(len(id) > 0)


if __name__ == '__main__':
    unittest.main()
