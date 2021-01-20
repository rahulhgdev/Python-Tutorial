def pop(list):
    def get_last_item(my_list):
        return my_list[len(list) - 1]

    list.remove(get_last_item(list))
    return list

a = [1,2,3,4,5]
print(pop(a))
print(pop(a))
print(pop(a))