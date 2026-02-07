from calendar import different_locale

my_set = {1, 2, 3}

print(my_set)

my_set1 =()

set1 = {2, 3, 5}
print(set1)
my_set2 =()
set2 = {6, 3, 8}
print(set2)

union_result = set1.union(set2)
union_result_operator = set2 | set1

print(union_result)

print(union_result_operator)

intersection_result = set1.intersection(set2)

intersection_result_operator = set1 & set2
print(intersection_result)
print(intersection_result_operator)

difference_result = set1.difference(set2)
difference_result_operator = set2 - set1
print(difference_result)
print(difference_result_operator)

symmetric_difference_result = set1.symmetric_difference(set2)
symmetric_difference_operator = set2 ^ set1

print(symmetric_difference_result)
print(symmetric_difference_operator)

# set methods
set3 = {1, 2, 3}

#add
set3.add(4)
print(set3)

#remove
set3.remove(2)
print(set3)

#discard  me hek element edhe nese nuk o nuk qet error
set3.discard(5)
print(set3)

#clear mi hek krej elementet
set3.clear()
print(set3)

#set with arry
my_list = [1, 2, 3, 3, 4, 4, 5]

unique_set = set(my_list)
unique_array = list(unique_set)

print(unique_array)


user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "cooking", "reading"}

common_interest = user1_interests.intersection(user2_interests)
print(common_interest)

#in

movies = "movies"
print(movies in user1_interests)

cooking = "cooking"
print(cooking in user1_interests)

#not in
print(movies not in  user1_interests)
print(cooking not in  user1_interests)


cos_users = {"Milot", "Dren", "Uvejsi"}
Uvejsi = "Uvejsi"
print(Uvejsi in cos_users)
Profa = "Profa"
print(Profa in cos_users)
