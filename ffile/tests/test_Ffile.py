from pathlib import Path
import pytest
from ..ffile import Ffile

local_path = Path(__file__).parent.absolute()


def test_missing_argument():
    # This is the wrong param, should be a!
    params = {"b": 1}
    math_file = Ffile(local_path / "math_file.txt", params)
    with pytest.raises(NameError):
        print(math_file.f())


def test_basic_math_locals():
    a = 1
    math_file = Ffile(local_path / "math_file.txt", locals())
    assert math_file.f() == "a = 1\n2*a = 2"

    # If we change a and re-define math_file, it will update output
    a = 2
    math_file = Ffile(local_path / "math_file.txt", locals())
    assert math_file.f() == "a = 2\n2*a = 4"

    # If we do not re-define math_file, it will not update output
    a = 4
    assert math_file.f() == "a = 2\n2*a = 4"


def test_basic_math_dict():
    params = {"a": 1}
    math_file = Ffile(local_path / "math_file.txt", params)
    assert math_file.f() == "a = 1\n2*a = 2"

    params = {"a": 2}
    math_file = Ffile(local_path / "math_file.txt", params)
    assert math_file.f() == "a = 2\n2*a = 4"

    params = {"a": 2, "b": "this does not matter"}
    math_file = Ffile(local_path / "math_file.txt", params)
    assert math_file.f() == "a = 2\n2*a = 4"


def test_basic_string():
    params = {"name": "Matt"}
    str_file = Ffile(local_path / "string_file.txt", params)
    assert str_file.f() == "My name is Matt.\nI SAID MY NAME IS MATT!!"


def test_import_local():
    import math

    imported_file = Ffile(local_path / "import_file.txt", locals())
    assert imported_file.f() == "this is a test: 3.14159"


def test_missing_import_local():
    imported_file = Ffile(local_path / "import_file.txt", locals())
    with pytest.raises(NameError):
        imported_file.f()
