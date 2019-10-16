import sys
import os

class Ffile:
    def __init__(self, file_name, local_vals):
        with open(file_name, 'r') as fp:
            self.string = fp.readlines()
        self.locals = local_vals

    def f(self):
        locals().update(self.locals)
        _formatted = []
        for _line in self.string:
            _formatted.append(eval(f"f'''{_line}'''"))
        return ''.join(_formatted)

def cli():
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print('Usage:')
        print('')
        print('ffile your_template_file key1=value key2=value')
        return
    
    for arg in sys.argv:
        if arg.find('=') > 0:
            try:
                exec(arg)
            except NameError:
                # If the key should be a string, it will throw a NameError
                key, val = arg.split('=')
                exec(f'{key} = "{val}"')

    if os.path.exists(sys.argv[1]):
        template = Ffile(sys.argv[1], locals())
        print(template.f())
    else:
        print(f'{sys.argv[1]} is not a valid file path')
