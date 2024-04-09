
# from G import Settings
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


#  help              Show this information
#  read              Read the value of a key
#  list              List the contents of a dir
#  write             Change the value of a key
#  reset             Reset the value of a key or dir
#  compile           Compile a binary database from keyfiles
#  update            Update the system databases
#  watch             Watch a path for changes
#  dump              Dump an entire subpath to stdout
#  load              Populate a subpath from stdin

