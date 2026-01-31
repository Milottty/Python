my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"

}

contact_info = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "charlie": "555-7124"
}
print(contact_info)
alice_phone = contact_info["Alice"]
print("Alice's phone number is:", alice_phone)

bob_phone = contact_info["Bob"]
print("Bob's phone number is:", bob_phone)

contact_info["Alice"] = "555-5342"
print("Alice's phone number is:", contact_info["Alice"]) #ME ndyshu numrin

contact_info["Dreni"] = "555-5555" #me shtu
print(contact_info)

del contact_info["Bob"]
print(contact_info)

#Get all keys
keys = contact_info.keys()
print(keys)

#get all value
value = contact_info.values()
print(value)

#get all items
items = contact_info.items()
print(items)

#Dictionary methods:
#clear() - removes all items from the dictionary
#copy() - returns a shallow copy of the dictionary
#get() - returns the value for a specified key
#items() - returns a view object of the dictionary's key-value pairs
#keys() - returns a view object of the dictionary's keys
#pop() - removes the item with the specified key and returns its value
#popitem() - removes and returns the last inserted key-value pair
#update() - updates the dictionary with elements from another dictionary or iterable
#values() - returns a view object of the dictionary's values

contact_information = {
    "Milot": {
    "phone_number": "555-5555",
    "email": "milot@gmail.com",
    "home_addres": "Lipjan",
    "birthdate": "2000/02/04"
    },
"Dreni": {
    "phone_number": "535-5555",
    "email": "dreni@gmail.com",
    "home_addres": "Prishtin",
    "birthdate": "2000/02/04"
    }
}



print(contact_information)