"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support get and put operations at constant time O(1) complexity.

get(key): Get the value (which will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value): Set or insert the value if the key is not already present. When the cache reaches its capacity, 
it should invalidate the least recently used item before inserting a new item.
"""

class LRUCache:

  class DLL:
      def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
  def __init__(self, capacity):
    self.m = {}
    self.capacity = capacity
    self.size = 0
    self.head = self.DLL(0,0)
    self.tail = self.DLL(0,0)
    self.head.next = self.tail
    self.tail.prev = self.head

  def get(self, key):
    if key in self.m:
      node = self.m[key]
      
      # remove node from current position
      node.prev.next = node.next
      node.next.prev = node.prev
      node.next = self.head.next

      # move the node to the head as the most recently used
      self.head.next.prev = node
      self.head.next = node
      node.prev = self.head
      return node.val
    return -1
  def put(self, key, value):
        # check if key already exists
        if key in self.m:
           # remove node from current position, and move it to the head as the most recently used
            self.get(key)

            # update the value
            self.m[key].val = value
            return
        self.size += 1
        # if the cache is full, remove the least recently used node
        if self.size > self.capacity:
            # delete the least recently used node from the hash map
            del self.m[self.tail.prev.key]
            # make the second last node the new tail
            self.tail.prev.val = self.tail.val
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1
        # create the new node
        new_node = self.DLL(key, value)
        # add the new node to the head as the most recently used
        self.head.next.prev = new_node
        new_node.next = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        # add the new node to the hash map
        self.m[key] = new_node

#Driver code
inputs = [10]
inputs1 = [["LRUCache put put get put get put get get get","2","1,1","2,2","1","3,3","2","4,4","1","3","4"]]
for i in range(len(inputs)):
    n = int(inputs[i])
    operations = [x for x in inputs1[i][0].split()]
    arr = [[int(x) for x in inputs1[i][j+1].split(',')] for j in range(n)]
    lru = None
    res = []
    for j in range(n):
        if operations[j] == "LRUCache":
            lru = LRUCache(arr[i][0])
            res.append('null')
        elif operations[j] == "get":
            res.append(str(lru.get(arr[j][0])))
        elif operations[j] == "put":
            lru.put(arr[j][0], arr[j][1])
            res.append('null')
    actual_output = ' '.join(x for x in res)
    print("LRU Cache :",actual_output)
# LRU Cache : null null null 1 null -1 null -1 3 4