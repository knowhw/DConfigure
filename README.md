



# #DConfigure
dconf is read, write, key list, load, dump, dir watch and database export module. it work on the system database.<br/>

## Installation
~~~bash
git clone https://github.com/knowhw/DConfigure.git

~~~

## Module usage
~~~python
from D import Configure


test = Configure("/net///launchpad/plank/docks//dock1/")
contents = test.contents()
# list the contents of a dir
print(contents)


item = test.getvalue("////icon-size///test")
# Read the value of a key


print(item)

item = test.setvalue("icon-size", 32)
print(item)

for item in test.watch():
	print(item)


#  read              Read the value of a key
#  list              List the contents of a dir
#  write             Change the value of a key
#  watch             Watch a path for changes
#  dump              Dump an entire subpath to stdout
#  load              Populate a subpath from stdin

~~~




