### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - LOOPs - UNIQUE LIST
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Your task is to write a program which removes all the number repetitions from the list.
# The goal is to have a list in which all the numbers appear not more than once.
### OBJECTIVE ###

#####################
###     CODE      ###
#####################

# Print the program title
print('''
#######################
###      UNIQUE     ###
###       LIST      ###
###       EVAL      ###
#######################
''')

### VARs & DEFs ###

#LIST DECLARATION
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

### MANUAL METHOD - DEPRECATED METHOD###
# my_list.sort()
# 
# index = 0
# indexNext = 1
# count = 0
# FOR LOOP
# while count < (len(my_list)):
#     if my_list[index] == my_list[indexNext]:
# 
#         print("DUPLICATED DETECTED")
#         del my_list[index]
#         index += 1
#         count += 1
#     elif my_list[index] != my_list[indexNext]:
#         print("NO DUPLICATE")
#         index += 1
#         count += 1
#     elif index > len(my_list):
#        break
#     else:
#         print("ERROR DETECTED")
### MANUAL METHOD - DEPRECATED METHOD ###

### IN METHOD ###
for i in my_list:
    if my_list.count(i) > 1:
        my_list.remove(i)




### SET METHOD - SUPERIOR METHOD ###
# print(set(my_list))
### SET METHOD - SUPERIOR METHOD ###


print("The list with unique elements only:")
print(my_list)


