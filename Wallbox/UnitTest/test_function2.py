import pytest
import os
from unittest.mock import patch
from Wallbox.FunctionsToTest.function2 import *

def test_findFirstAdminExecutableLessthan14MB_Exception():
    with pytest.raises(Exception):
        assert findFirstAdminExecutableLessthan14MB("")

def test_findFirstAdminExecutableLessthan14MB_NotFound(tmp_path):
    assert findFirstAdminExecutableLessthan14MB(tmp_path) == "File not found"

def test_test_findFirstAdminExecutableLessthan14MB():
    assert findFirstAdminExecutableLessthan14MB(".\\UnitTest") == ".\\UnitTest\\test_function1.py"

def test_test_findFirstAdminExecutableLessthan14MB_bigFiles():
    with patch('os.path.getsize') as size_mock:
        size_mock.return_value = 14*(2**20) + 1
        assert findFirstAdminExecutableLessthan14MB(".\\UnitTest") == "File not found"

def test_test_findFirstAdminExecutableLessthan14MB_notExecutable():
    with patch('os.access') as access_mock:
        access_mock.return_value = False
        assert findFirstAdminExecutableLessthan14MB(".\\UnitTest") == "File not found"