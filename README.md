



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
## getvalue
`Read` veritabanından belirli bir ayarın değerini okumak için kullanılır. 
## setvalue
`Write` veritabanına belirli bir ayarın değerini yazmak veya değerini değiştirmek, güncellemek için kullanılir.

## contents
`Key List` veritabanındaki tüm anahtarları (keys) listelemek, sistemin yapılandırmasını anlamak veya denetlemek için kullanılabilir.

## watch
`Path Watch` belirli bir dizini izleyerek veritabanındaki değişiklikleri algılamak. Sistem yapılandırmasının dinamik olarak güncellenmesini sağlar.

## load
`Load` Özellikle yapılandırma dosyalarını yüklemek veya başka bir sistemden veri almak için kullanışlıdır.

## dump
`Dump` veritabanını bir dosyaya dışa aktarmak yapılandırmaları yedeklemek veya başka bir sistemle paylaşmak için kullanılabilir.

## export
`Database Export` veritabanını başka bir formata dönüştürmek veya başka bir sistemle entegre etmek için kullanılır. 



