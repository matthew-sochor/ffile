from pathlib import Path
import pytest
from ..ffile import Ffile
from subprocess import check_output, CalledProcessError

local_path = Path(__file__).parent.absolute()


def test_missing_file():
    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'notafile.txt'}", "--vars", "a=2"])


def test_too_few_args():
    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'notafile.txt'}"])

    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'notafile.txt'}", "--vars"])

    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'notafile.txt'}", "--json"])

    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'notafile.txt'}", "--yaml"])


def test_incorrect_second_arg():
    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'notafile.txt'}", "--whatisthis", "x=5"])


def test_missing_argument_vars():
    # This is the wrong param, should be a!
    with pytest.raises(CalledProcessError):
        check_output(["ffile", f"{local_path / 'math_file.txt'}", "--vars", "b=2"])


def test_basic_math_vars():
    math_file = check_output(
        ["ffile", f"{local_path / 'math_file.txt'}", "--vars", "a=1"]
    )
    assert math_file.decode("utf-8") == "a = 1\n2*a = 2\n"

    # If we change a and re-define math_file, it will update output
    math_file = check_output(
        ["ffile", f"{local_path / 'math_file.txt'}", "--vars", "a=2"]
    )
    assert math_file.decode("utf-8") == "a = 2\n2*a = 4\n"


def test_basic_string_vars():
    str_file = check_output(
        ["ffile", f"{local_path / 'string_file.txt'}", "--vars", "name=Matt"]
    )
    assert str_file.decode("utf-8") == "My name is Matt.\nI SAID MY NAME IS MATT!!\n"


def test_missing_file_json():
    # This is the wrong param, should be a!
    with pytest.raises(CalledProcessError):
        check_output(
            ["ffile", f"{local_path / 'math_file.txt'}", "--json", "notafile.json"]
        )


def test_wrong_file_type_json():
    # This is the wrong param, should be a!
    with pytest.raises(CalledProcessError):
        check_output(
            [
                "ffile",
                f"{local_path / 'math_file.txt'}",
                "--json",
                f"{local_path / 'params.yaml'}",
            ]
        )


def test_basic_math_json():
    math_file = check_output(
        [
            "ffile",
            f"{local_path / 'math_file.txt'}",
            "--json",
            f"{local_path / 'params.json'}",
        ]
    )
    assert math_file.decode("utf-8") == "a = 1\n2*a = 2\n"


def test_basic_string_json():
    str_file = check_output(
        [
            "ffile",
            f"{local_path / 'string_file.txt'}",
            "--json",
            f"{local_path / 'params.json'}",
        ]
    )
    assert str_file.decode("utf-8") == "My name is Matt.\nI SAID MY NAME IS MATT!!\n"


def test_missing_file_yaml():
    # This is the wrong param, should be a!
    with pytest.raises(CalledProcessError):
        check_output(
            ["ffile", f"{local_path / 'math_file.txt'}", "--yaml", "notafile.yaml"]
        )


def test_basic_math_yaml():
    math_file = check_output(
        [
            "ffile",
            f"{local_path / 'math_file.txt'}",
            "--yaml",
            f"{local_path / 'params.yaml'}",
        ]
    )
    assert math_file.decode("utf-8") == "a = 1\n2*a = 2\n"


def test_basic_string_yaml():
    str_file = check_output(
        [
            "ffile",
            f"{local_path / 'string_file.txt'}",
            "--yaml",
            f"{local_path / 'params.yaml'}",
        ]
    )
    assert str_file.decode("utf-8") == "My name is Matt.\nI SAID MY NAME IS MATT!!\n"
