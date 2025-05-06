dictionary = dict()
print("Empty Dictionary:" ,dictionary)
a = int(input ("Number of items: "))
for i in range(a):
	key = input("key: ")
	value = input("value: ")
	dictionary[key]=value
print("Dictionary:", dictionary)
key = input("Enter the key to update: ")
if key in dictionary:
	value = input("Enter the new value: ")
	dictionary[key]=value
	print("Value updated")
else:
	print("Key not found")
key = input("Enter the key to retrieve: ")
if key in dictionary:
	print (f"Key: {key}, Value: {dictionary[key]}")
else:
	print ("Key not found")
key = input("Enter the key to get using the get() method: ")
if key in dictionary:
	print (f"Key: {key}, Value: {dictionary.get(key)}")
else:
	print ("Key not found")
key = input("Enter the key to delete: ")
if key in dictionary:
	dictionary.pop (key)
	print ("Deleted")
else:
	print ("Key not found")
print("Updated Dictionary:", dictionary)