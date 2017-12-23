import random
food_list = ["chicken wings", "french fries", "burger", "ice cream", "pizza", "toast"]
cookingstyle_list = ["Italian", "Chinese", "Vietnamese", "Hawaiian"]
adj_list = ["Delicious", "Crunchy", "Spicy", "Curry", "Juicy", "Sour", "Sweet and Sour"]


for i in range(10):
    print( adj_list[(random.randint(0,len(adj_list)-1))] + " " +
           cookingstyle_list[(random.randint(0,len(cookingstyle_list)-1))] + " "
           + food_list[random.randint(0,len(food_list)-1)])
