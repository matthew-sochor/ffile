print("Life before Ffile:")
print("")
# example the first
name = "Matt"
print(f"{name} is not the name of a good developer")

# example the second
name = "Matt"
adjective = "mediocre"
lines = [
    f"{name} is the name of some Browns fan. And they are a {adjective} football team.",
    "LAME!",
    "Not only that,"
    f"This dude {name.upper()} sounds like a {adjective.upper()} father!",
]
print("\n".join(lines))
print("")
print("Life after Ffile:")
print("")
# Ffile example
from ffile import Ffile

template = Ffile("template.txt")
template.print(name="Matt", adjective="not bad")
