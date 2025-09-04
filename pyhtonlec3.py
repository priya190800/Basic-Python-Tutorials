#LIST IN PYTHON
#we can store different types of data in single variable and can changeable
#ex= student=["karan",65.34,"surat",34]
# [ ] use square brackets 
marks1=85.09
marks2=89.64
marks3=67.3
marks4=78.56
marks5=26.34

marks=[12,34.5,32.45,23,34,78.65]      #list
print(type(marks))
print(marks[2])
print(marks[4])
print(len(marks))

student=["karan",65.34,"surat",34]
print(student)

#str="hello"
#print(str[0])     # python string can not change after assignment
#str[0]="y"

list=["hello"]
print(list[0])    #python list can change
list[0]="priya"
print(list)


#list slicing
marks=[34.56,65,43,24.78]
print(marks[1:2])
print(marks[0:3])
print(marks[::-1])

#list method
list=[23,45,65,45]
list.append(45.34)   #end element an end of list
print(list)

list=[23,45,65,45]
list.extend([56,78])   #add element of one list to another list
print(list)

list=[23,45,65,45]
list.insert(2,90)    # add element at specific index or position
print(list)

list=[23,45,65,45,2]
list.sort()           # sorts in ascending order like chadta kram ma
print(list)

list=[23,45,65,90,45]
list.sort(reverse=True)    #sorts in descending order like utrta kram ma
print(list)

list=[23,45,65,90,45]
list.reverse()    #reverse list
print(list)

list=[23,45,65,90,45]
list.remove(90)    # remove element of list that want remove
print(list)

list=[34,354,432,223]
list.pop(1)          #remove element at index or position
print(list)



#tuples in python
#built in data types that create immutable sequence of values and not changeable
#( ) use round brackets

tuple=(67,43,23,21.45,"hello")
print(type(tuple))
print(tuple[4])

tuple=()
print(tuple)  #empty tuple

#tuple slicing
tuple=(67,43,23,21.45,"hello")
print(tuple[2:])

#tuple methods
tuple=(67,43,23,21.45,"hello")
print(tuple.index("hello"))     #return the position of given elements
print(tuple.index(43))

tuple=(67,43,23,67,21.45,"hello")
print(tuple.count(67))   # count the total elements  of given number , how many numbers of elements


#questions
#1 ask user to enter name of 3 movie and store them in list
movie=[]
list1=(input("enter 1st movie="))
list2=(input("enter 2nd movie="))
list3=(input("enter 3rd movie="))
movie.append(list1)
movie.append(list2)
movie.append(list3)
print(movie)


#2nd way 
movie=[]
movie.append(input("enter 1st movie="))
movie.append(input("enter 2nd movie="))
movie.append(input("enter 3rd movie="))
print(movie)

#2 question  check list contain palindrome number 
# palindrom means [1,2,3] list ne copy krine [1,2,3] aave and aene revers krvi to [3,2,1] aave thats not match to the original list that's called not palindrome number if match that called palindrome number

list1=[1,"abc","abc",1]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("this is a palidrome list")
else:
     print("this is not palidrome list")


#3rd question 
tuple=("C","D","A","A","B","B","A")
print("the number of student=",(tuple.count("A")))

#4th question
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)


