#Create a superlist using class and change the len function to return 1000

class Superlist(list):
    def __len__(self):
        return 1000

super_list1 = Superlist();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))