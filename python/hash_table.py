
class HashTable:
	def __init__(self, _max = 10):
		self.MAX = _max
		self.items = [[] for _ in range(self.MAX)]
	def hash(self, key):
		h = 0
		for char in key:
			h += ord(char)
		return h % self.MAX
	
	def __setitem__(self, key, value):
		h = self.hash(key)
		for idx, kv in enumerate(self.items[h]):
			if kv[0] == key:
				self.items[h][idx] = (key, value)
				return
		self.items[h].append((key, value))

	def __getitem__(self, key):
		h = self.hash(key)
		el = self.items[h]
		for k , v in el:
			if k == key: return v

	def __delitem__(self, key):
		h = self.hash(key)
		items  = self.items[h]
		for i, kv in enumerate(items):
			if kv[0] == key:
				del items[i]
	



d = HashTable()
print(d.items)
d["march 6"] = 5
d["march 17"] = 6
d["march 18"] = 7

print(d.items)

del d["march 17"]

print(d.items)
print(d)