#QUESTION 1:
#This function takes the input of the user and prints
#"Hello, " plus the users name

def helloUser(userName):                #creation of function
    user = userName                     #makes a variable for the paramenter
    print("Hello, " + user)             #prints personalized message
helloUser(input("What's your name? "))  # Takes the input from the user


#QUESTION 2:
#This function takes goes through numbers 1 to 100 and 
#prints back the ones that are divisible by 2

def firstOdds ():                   #function creation
    for numbers in range (1,101):   #makes a for function with range of 1 to 100
        if numbers % 2 == 0:        #if the number is divisible by 2
            print(numbers)          #print it
firstOdds()                         #calling the function




#QUESTION 3: 
# This program creates a function that returns
#the max number in a list. The print command is there to 
#see the return result
def maxNumInList (numList):    # maxNumInList is created wiht a list for an argument
    alist = numList             # the list varaible copies the numList parameter
    return (max(alist))         # the function returns the max number of the alist list
aList = [1, 2, 3, 8, 4 ,5]      # example list 
print(maxNumInList(aList))      # the function is called. print is used to make sure the function works




#QUESTION 4:
#This function takes an input year. If the year is divisible 
#by 4 but not 100, or is divisible by 400, it will return
#true. Otherwise, it returns false. The print function is 
#there to test the output
def leapYear (year):                     #function is created wiht the year as parameter       
    year = int(year)                     #a variable is created to store the input    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # if the year is divisible by 4 and not 100 or is divisible by 400
        return True                         # return true
    else:                               #otherwise
        return False                    #return false
print(leapYear (input("Input Test Year ")))  #call the function. print function is there to test the return value




#QUESTION 5:
#This function takes a list as a parameter and goe through it
#if a the elements in the list are consecutive, it will return true
#otherwise it returns false

def consecutiveNumbers(aList):                  #defining the function with aList as a parameter
    list = aList                        #making a variable for the list
    i = 0                           #using i as a counter to go through the list
    for number in range (i, len(list)):  #making a for loop with the ranges 0 to the end of the list
        if list[i] + 1 == list[i + 1]: #if an element in the list at coutner i + 1 is = to the same coutner i +1
            i = i + 1             #make i = i+1 for the next iteration
            return True             #if all iterations go through as True, return ture
        else:                       #otherwise
            return False            #return false
list = [1, 2, 3, 4, 5]           #example list
print(consecutiveNumbers(list))  #calling the function. print function there for example
