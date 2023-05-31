#Exercise 1
#Using the given list, print out a filtered version of the list with only the numbers that are less than ten

def exercise_1():
    alist_local = alist
    for number in alist_local:
        if number < 10:
            print(number)
    
alist = [1,11,14,5,8,9]
exercise_1()
print()


#Exercise 2
#Merge and sort the two lists below
#Hint: You can use the .sort() method
def exercise_2():
    l_1_local = l_1
    l_2_local = l_2
    L3 = l_1_local + l_2_local
    L3.sort()
    print(L3)

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
exercise_2()
print()


#Exercise 3 
#Square every number from 1 to 15 
def exercise_3():
    for i in range(1, 16):
        print(i**2)

exercise_3()
print()


#Exercise 4 
#Using List Comprehension and the given list, 
#Print out a filtered list with only the names that start with the letter 'a'. 
#The names in the outputted list should be title cased and have no whitespace.
def exercise_4(names_list):
    a_team=[]
    for i in names_list:
        i = i.strip().title()
        if i.startswith("A"):
            a_team.append(i)
    return a_team

print(exercise_4(['   amy', 'Briant', 'Ryan ', ' Alex', 'steve', '  ']))
#expected output = ['Amy', 'Alex']
print()


#Exercise 5 
#Print all Prime numbers from 1 to 100
def exercise_5(): 
    primes=[]
    for i in range(1,101):
        prime = True
        for num in range(2,i):
            if i % num == 0:
                prime = False
        if prime:
            primes.append(i)
    print(primes)
exercise_5()

