from random import random


class RandomizedSet:
    """
    In python, creating a simple api for a set() would be a perfect solution if not for the third operation, getRandom().
     We know that we can retrieve an item from a set, and not know what that item will be, but that would not be actually random.
     This is due to the way python implements sets. In python3, when using integers, elements are popped from the set in the order they appear in the underlying
hashtable. Hence, not actually random.)

    A set is implemented essentially the same as a dict in python, so the time complexity of add / delete is on average O(1). When it comes to the random function, however, we run into the problem of needing to convert the data into a python list in order to return a random element. That conversion will add a significant overhead to getRandom, thus slowing the whole thing down.

    Instead of having to do that type conversion (set to list) we can take an approach that involves maintaining both a list and a dictionary side by side. That might look something like:

    data_map == {4: 0, 6: 1, 2: 2, 5: 3}
    data == [4, 6, 2, 5]

    Notice that the key in the data_map is the element in the list, and the value in the data_map is the index the element is at in the list.
    """

    def __init__(self):
        self.hash_map = dict()
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        else:
            self.hash_map[val] = len(self.data)
            self.data.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        else:
            last_elem_in_list = self.data[-1]
            index_of_elem_to_remove = self.hash_map[val]

            self.hash_map[last_elem_in_list] = index_of_elem_to_remove
            self.data[index_of_elem_to_remove] = last_elem_in_list

            self.data[-1] = val

            self.data.pop()

            self.hash_map.pop(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(4))
print(obj.insert(3))
print(obj.insert(2))
print(obj.remove(3))
# print(obj.getRandom())
