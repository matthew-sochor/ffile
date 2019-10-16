# Ffile: f-strings in a file
*The thing you never asked for, but that you got anyway*

## What are f-strings?  
Not sure how you got here without knowing that, but in short, its the new way to format strings in python as of 3.6!  Which isn't that new.  Its been out a while.  Like google it, there are tons of resources on why f-strings are cool.

## I know f-strings are cool, so whats this then?
You can do a single line f-strings like this:

```python
name = 'Matt'
print(f"{name} is not the name of a good developer")
```

*sublime*

but multi-line f-strings are ugly:
```python
name = "Matt"
adjective = "mediocre"
lines = [
    f"{name} is the name of some Browns fan. And they are a {adjective} football team.",
    "LAME!",
    "Not only that,"
    f"This dude {name.upper()} sounds like a {adjective.upper()} father!",
]
print("\n".join(lines))
```

Yikes! Harsh f-string! And that needed a real weird thing with new-lines.

Also, what if you want to parameterize a long file?  Several hundred or thousand lines? No thanks. 

## F-strings on a file would be cool
Lets throw that text into a file, lets call it "template.txt" which coincidentally exists in this very repository:

```
{name} is a good developer!
His kids love him deeply because he is a {adjective} father!

They definitely do NOT say:

"Hey {name.upper()}! you are {adjective.split(' ')[-1]} at parenting!"
  - {name.lower()}'s kids, probably
```

Boy it would be cool to take a big complex document, parametrize it like an f-string, and even run some simple python in it!

```python
template = Ffile("template.txt")
template.print(name="Matt", adjective="not bad")
```

*sublime*

Also, maybe just do don't want to print, and you just want that formatted string

```python
formatted = template.f(name="Matt", adjective="not bad")
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