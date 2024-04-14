
from os import system
from subprocess import call

from os import popen 



class Configure(str):
	
	def __init__(self, path):
		
		self.path = chr(47).join( [  item for item in self.split("/") if item ] )
		# path: net/launchpad/plank/docks/dock1
		

	def _convert2str(self, value):
		
		import json
		dump = json.dumps(str(value))
		value =  "false" if dump == '"False"' else ( "true" if dump == '"True"' else dump ) 

		return value
		
	def _split(self, key):
		
		key = [  item for item in key.split("/") if item  ]
		# test.getvalue("////icon-size/test")
		key = key [0] if len(key) > 1 else ( key [0] if key else None  )
		# ['icon-size', 'test']
		return key
	def setvalue(self, key, value):

		system("%s /%s/%s %s" % ("dconf write", self.path, self._split(key), self._convert2str(value)))
		
		return self.path, self._split(key), self._convert2str(value)
		# change the value of a key

	
	def getvalue(self, key):
		
		key = [  item for item in key.split("/") if item  ]
		# test.getvalue("////icon-size/test")
		key = key [0] if len(key) > 1 else key [0]
		# ['icon-size', 'test']
		
		
		item = popen("dconf read /%s/%s" % (self.path, key)).read()
		# read the value of a key
		
		return item.strip()
		
	def contents(self):
		
		dirs = [ item for item in self.path.split(chr(47)) if item ]
		contentlist = popen("%s %s" % ("dconf list", "/%s/" % chr(47).join(dirs))).readlines()
		# list the contents of a dir
		
		
		return [ key.strip() for key in contentlist ]	

	
	def export(path, dump):
		with open(path, "w") as f :  f.write(dump)
	def watch(self):
		# watch a path for changes
		
		for item in call(["dconf", "watch", "/%s" % self.path]):
			# subprocess.call
			yield item
	def load(d, ini):
		system("%s %s < %s" % ("dconf load", d, ini))
		# populate a subpath from stdin

	
	def dump(directory):
		return popen("%s %s" % ("dconf dump", directory)).read()
		# dump an entire subpath to stdout
		
		
