from pathlib import Path
import pytest
from ..ffile import Ffile
from subprocess import check_output, CalledProcessError

local_path = Path(__file__).parent.absolute()


def test_missing_argument():
    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'math_file.txt'}"])

    # This is the wrong param, should be a!
    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'math_file.txt'}", "b=2"])


def test_basic_math_vars():
    math_file = check_output(["ffile", f"{local_path / 'math_file.txt'}", "a=1"])
    assert math_file.decode("utf-8") == "a = 1\n2*a = 2\n"

    # If we change a and re-define math_file, it will update output
    math_file = check_output(["ffile", f"{local_path / 'math_file.txt'}", "a=2"])
    assert math_file.decode("utf-8") == "a = 2\n2*a = 4\n"
