print("Life before Ffile:")
print("")
# example the first
name = "Matt"
x = f"{name} is not the name of a good developer"
print(x)

# example the second
name = "Matt"
adjective = "mediocre"
x = [
    f"{name} is the name of some Browns fan. And they are a {adjective} football team.",
    "LAME!",
    "Not only that,"
    f"This dude {name.upper()} sounds like a {adjective.upper()} father!",
]
print("\n".join(x))
print("Life after Ffile:")
print("")
# Ffile example the first
from ffile import Ffile

params = {"name": "Matt", "adjective": "not bad"}
template = Ffile("template.txt", params)
templated_file = template.f()
print(templated_file)

print("Say it louder for the people in the back!")
print("")
# Ffile example the second
name = "Matt"
adjective = "not bad"
template = Ffile("template.txt", locals())
template.print()
