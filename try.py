#STRING




# 1.Write a program to remove all vowels from a string.

# vowels=['a','A','e','E','i','I','o','O','u','U']
# a=input("enter a string")
# result=''
# for i in a:
#     if i not in vowels:
#         result=result+i

# print(result)

# 2. Create a program to count the number of words in a sentence.

# a=input("enter a sentence")
# word=a.split()
# print(len(word))


# 3. Develop a program that finds the longest word in a sentence.

# a=input("enter a sentence")
# word=a.split()
# large=''
# for i in word:
#     if len(i)>len(large):
#         large=i
# print(large)



# 4. Write a program to check if two strings are anagrams (e.g., "listen" and "silent").

# s1=input("enter a string")
# s2=input("enter another one")
# s1=s1.lower()
# s2=s2.lower()

# s1=sorted(s1)
# s2=sorted(s2)
# if s1==s2:
#     print("anagrams")
# else:
#     print("not anagrams")


# 5. Implement a program that replaces all spaces in a string with underscores.


# sen=input()
# z=sen.replace(' ','_')
# print(z)



#   Tuples 

# 1.Create a program to multiply all numbers in a tuple.


# tuples=(1,2,3,4)
# mul=1
# for i in tuples:
#     mul=mul*i
# print("the result is =",mul)



# 2. Develop a program that returns the maximum and minimum values from a tuple of numbers.


# tuples=(1,2,3,4)
# min=tuples[0]
# max=tuples[0]
# for i in tuples:
#     if i>max:
#         max=i
#     if i<min:
#         min=i
# print(min)
# print(max)


# 3. Implement a program that finds the repeated items in a tuple.
# tuples=(1,2,3,4,4)
# result=()
# repeat=()
# for i in tuples:
       
#         if i in result and i not in repeat:
#               repeat=repeat+(i,)
#         result=result+(i,)
# print("the repeated items are=",repeat)


# Dictionaries 
#1.Write a program to find the key with the maximum value in a dictionary.

# dict={'first':2,'second':2,'third':3}
# max_val=0
# max_key=''
# print(dict.values())
# for keys,value in dict.items():
#     if value>max_val:
#         max_val=value
#         max_key=keys
# print(max_key)

# 2. Write a program that filters out dictionary items where the value is less than a given number.


# n=5
# my_dict={'first':2,'second':8,'third':9}
# new={}
# for key,value in my_dict.items():
#     if value>=n:
#         new[key]=value
# print(new)

#Lists
# 1. Write a program that rotates a list to the left by k positions.
#  Could not solve

# 2. Write a program to find the second largest number in a list.

# my_list=[2,3,4,5]
# largest=1
# sec_last=largest
# for i in my_list:
#     if i>largest:
#         largest=i
# could not solve

#3. Write a program to remove all even numbers from a list of integers.

# list=[1,2,3,4,5]
# new_list=[]
# for i in list:
#     if i%2==0:
#         new_list.append(i)
# print(new_list)

