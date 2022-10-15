#hello function
def hello():
        print("Hello user")


#list function
def pack(item1, item2, item3):
        return [item1, item2, item3]


#eat lunch function
def eat_lunch(user_list):
        if len(user_list) == 0:
                print("My lunchbox is empty!")
        else:
                for i in range(len(user_list)):
                        if i == 0:
                                print(f"First I eat {user_list[0]}")
                        else:
                                print(f"Next I eat {user_list[i]}")


#call functions
hello()
print(pack("Shoes", "Socks", "Clothes"))
eat_lunch(["Sandwich", "Apple", "Salad"])