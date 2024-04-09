

<div align="right">

[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

</div>

<br/>

# #python3-dconf Python Module
dconf is read, write, key list, load, dump, dir watch and database export module. it work on the system database.<br/>

## Installation
~~~bash
git clone https://github.com/knowhw/python3-dconf.git
sudo cp -R python3-dconf/conf /usr/local/lib/python3.10
~~~

## Module usage
~~~python
import conf

directory = '/net/launchpad/plank/docks/dock1/icon-size'
conf.write(directory, 34)
size = conf.read(directory)
print(size)
...

directory = '/net/launchpad/plank/docks/dock1'
listkey = conf.listkey(directory)
print(listkey)
...
~~~




