#without using yield
even_list = []
# def even_number_genarator(limit):
#     for i in range (2, limit+1, 2):
#         even_list.append(i)
#     return even_list

# print(even_number_genarator(10))


def even_number_genarator(limit):
    for i in range (2, limit+1, 2):
        yield i

for num in even_number_genarator(12):
    print(num)



