student1_lunchbox = {"dosa","idly","sambar","chitney","dosa"}
student2_lunchbox = {"maggi","fried rice","dosa"}
print("student 1 lunch box",student1_lunchbox)
print("student 2 lunch box",student2_lunchbox)

student1_lunchbox.add("sagu")
print("student 1 luch box after adding sagu",student1_lunchbox)

common_items = student1_lunchbox.intersection(student2_lunchbox)
print("common food items in both lunch box",common_items)

import array as a
food_count =  a.array("i",[3,5,2,4])
print("food count array",food_count)

food_count.insert(4)
print("food count after adding 4",food_count)

count_of_4 = food_count.count(4)
print("food count of 4",count_of_4)

print("================= luch box organsier =================")
print("lunch box 1",student1_lunchbox)
print("lunch box 2",student2_lunchbox)
print("shared food",common_items)
print("food count",food_count)
print("=======================================================")