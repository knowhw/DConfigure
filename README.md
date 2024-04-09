



# #DConfigure


`DConfigure`, GNOME (GNU Network Object Model Environment) masaüstü ortamında kullanılan bir sistem ayarları yönetim aracıdır. Bu araç, kullanıcıların tercihlerini, yapılandırmalarını ve ayarlarını kaydetmek için bir veritabanı gibi calisir.


<br/>

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


~~~


