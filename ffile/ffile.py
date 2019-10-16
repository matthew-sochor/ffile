import sys
import os
import yaml
import json
from typing import Union, Dict
from pathlib import Path


class Ffile:
    """Ffile applies f-string syntax to a file
    """

    def __init__(self, file_name: Union[str, Path], local_vals: Dict):
        """Initialize Ffile
        
        Arguments:
            file_name {Union[str, Path]} -- File to read and interpolate as an f-string
            local_vals {Dict} -- Values to use in interpolation
        """
        with open(file_name, "r") as fp:
            self.string = fp.readlines()
        self.locals = local_vals

    def f(self) -> str:
        """Format the FFile
        
        Returns:
            [str] -- f-string formatted file
        """
        locals().update(self.locals)
        _formatted = []
        for _line in self.string:
            _formatted.append(eval(f"f'''{_line}'''"))
        return "".join(_formatted)

    def print(self):
        """Format and print the FFile
        """
        print(self.f())


def cli():
    """Command line interface for Ffile (ffile)
    """
    if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage:")
        print("")
        print("Supply variables with key=value pairs")
        print("")
        print("ffile your_template_file --vars key1=value key2=value")
        print("")
        print("Or supply variables in a json file")
        print("")
        print("ffile your_template_file --json params.json")
        print("")
        print("Or supply variables in a yaml file")
        print("")
        print("ffile your_template_file --json params.json")
        return

    if os.path.exists(sys.argv[1]) == False:
        raise FileNotFoundError(f"Template file does not exist: {sys.argv[1]}")

    if len(sys.argv) < 3:
        raise SyntaxError("Incorrect arguments, please type 'ffile -h' for help")
    else:
        if sys.argv[2] == "--vars":
            params = {}
            for arg in sys.argv[3:]:
                if arg.find("=") > 0:
                    key, val = arg.split("=")
                    try:
                        exec(f"params['{key}'] = {val}")
                    except NameError:
                        # If the key should be a string, it will throw a NameError
                        exec(f"params['{key}'] = '{val}'")

                else:
                    raise SyntaxError(
                        "--vars input should be key=value pairs.  Missing ="
                    )

        elif sys.argv[2] == "--json":
            if os.path.exists(sys.argv[3]) == False:
                raise FileNotFoundError(f"Json file does not exist: {sys.argv[3]}")
            else:
                with open(sys.argv[3], "r") as fp:
                    params = json.load(fp)
        elif sys.argv[2] == "--yaml":
            if os.path.exists(sys.argv[3]) == False:
                raise FileNotFoundError(f"Yaml file does not exist: {sys.argv[3]}")
            else:
                with open(sys.argv[3], "r") as fp:
                    params = yaml.load(fp, Loader=yaml.FullLoader)
        else:
            raise SyntaxError(
                "Incorrect 2nd argument, must be one of --vars --json or --yaml, please type 'ffile -h' for help"
            )

        template = Ffile(sys.argv[1], params)
        template.print()

