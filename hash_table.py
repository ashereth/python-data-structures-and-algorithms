class HashTable:
    def __init__(self, size = 7) -> None:
        #create an empty list of length = size
        self.data_map = [None] * size
    #hash method to get address of where to store something
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    #add a key value pair to the hash table
    def set_item(self, key, value):
        #use hash function to get address index
        index = self.__hash(key)
        #if there isnt an empty list at that index make it one
        if self.data_map[index] == None:
            self.data_map[index] = []
        #add a list containing the key and value to the list at the index
        self.data_map[index].append([key, value])
    #search for an value using a key
    def get_item(self, key):
        #use hash function to get address index
        index = self.__hash(key)
        #if there is something at that index loop through the list to find key
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                #if the keys match return the value
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    #returns a list of all keys within the table
    def keys(self):
        #create a list to store all the keys
        all_keys = []
        #for all indices of data map
        for i in range(len(self.data_map)):
            #if there is a list at this index
            if self.data_map[i] is not None:
                # for all indices within the list at data_map[i]
                for j in range(len(self.data_map[i])):
                    #add the key to the list of keys
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
#function that returns true if there is an
#  item shared in the lists in  O(n) time
def item_in_common(list1, list2):
    mydict = dict()
    for i in list1:
        mydict[i] = True
    for i in list2:
        if i in mydict:
            return True
    return False

print("\n")
HT = HashTable()
HT.set_item("hello", "hello")
HT.set_item("bolts", 20)
HT.set_item("washers", 2314)
HT.print_table()
print(HT.get_item("washers"))
print(HT.keys())
print("There is at least one item in common between these two arrays:", item_in_common([1, 2, 3], [3]))
print('\n')