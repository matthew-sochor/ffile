# Ffile: f-strings in a file
*The thing you never asked for, but that you got anyway*

## What are f-strings?  
Not sure how you got here without knowing that, but in short, its the new way to format strings in python as of 3.6!  Which isn't that new.  Its been out a while.  Like google it, there are tons of resources on why f-strings are cool.

## I know f-strings are cool, so whats this then?
You can do a single line f-strings like this:

```python
name = 'Matt'
x = f'{name} is not the name of a good developer'
print(x)
```

but multi-line f-strings are U-G-L-Y
```python
name = "Matt"
adjective = "mediocre"
x = [
    f"{name} is the name of some Browns fan. And they are a {adjective} football team.",
    "LAME!",
    "Not only that,"
    f"This dude {name.upper()} sounds like a {adjective.upper()} father!",
]
print("\n".join(x))
```

Yikes! Harsh f-string! And that did a real weird thing with new-lines.

Also, what if you want to parameterize a long file?  Several hundred or thousand lines?  

## F-strings on a file would be cool
Lets throw that text into a file, lets call it "template.txt" which coincidentally exists in this very repository:

```
{name} is a good developer!
His kids love him deeply because he is an {adjective} father!

They definitely do NOT say:

"Hey {name.upper()}! you are {adjective.split(' ')[-1]} at parenting!"
  - {name.lower()}'s kids, probably
```

Boy it would be cool to take a big complex document, parametrize it like an f-string, and even run some simple python in it!

```python
from ffile import Ffile
params = {'name': 'Matt', 'adjective': 'not bad'}
template = Ffile('template.txt', params)
templated_file = template.f()
print(templated_file)
```

or maybe call it from local variables, which is a little closer to what you maybe expect from an f-string.  Also, maybe just do that format and print in one step.

```python
from ffile import Ffile
name = 'Matt'
adjective = 'not bad'
template = Ffile('template.txt', locals())
template.print()
```

don't believe me?  Well pip install this package:

`pip install ffile`

or from this repo:

`pip install .`

and then run:

`python example.py`

## Don't leave yet!  There is a CLI too!
You can also call ffile from the command line!

`ffile template.txt --vars name=Matt adjective='not bad'`

or you can put those variables in a json file:

`ffile template.txt --json params.json`

or what about yaml:

`ffile template.txt --yaml params.yaml`