import os

def test_main_py_exists():
    # Asserts that main.py is in the current directory
    assert os.path.isfile('main.py'), "main.py does not exist in the directory"
