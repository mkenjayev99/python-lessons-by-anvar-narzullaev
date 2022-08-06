# step 1

# User input logic

# n = int(input("Length of arr: "))
# collection_txt = []
# x = 0
# while True:
#     interlist = input("Enter a word: ")
#     collection_txt.append(interlist)
#     x += 1
#     if x == n:
#         break


# def capLetter(collection_txt):
#     for i in range(len(collection_txt)):
#         a = collection_txt.pop(i)
#         collection_txt.insert(i, a.capitalize())
#     return collection_txt

# # print(capLetter(['odil', 'qobil', 'komil'])) #This raw only for testing
        

# step 2

def bite_even(nums_here):
    nums_list = []
    for i in range(len(nums_here)):
        if nums_here[i] % 2 == 0:
            nums_list.append(nums_here[i])

    return nums_list

# print(bite_even([2, 5, 8, 7, 1, 6, 3, 4, 9, 12, 87]))
