#A collection of fizzBuzz like questions for interviews 

#1. FizzBuzz

def fizzBuzz(n):
    for i in range(1, n+1):
        res = ""

        if i % 3 == 0:
            res += "Fizz"

        if i % 5 == 0:
            res += "Buzz"

        else:
            print(i)
            continue

        print(res)

#2. Reverse a string

def strReverse(input_str):
    res = ""

    for char in input_str[::-1]:
        res += char
    
    print(res)

    #Using a stack 

    # resStack = []
    # for char in input_str:
    #     resStack.append(char)
    # res = ""

    # for i in range(len(input_str)):
    #     res += resStack.pop()

    # print(res)

#3. Find the minimum value in a list

def findMinVal(input_list):
    minVal = input_list[0]

    for num in input_list[1:]:
        if num < minVal: 
            minVal = num

    print(minVal)

#4. Find the maximum value in a list 

def findMaxVal(input_list):
    mavVal = input_list[0]

    for num in input_list[1:]:
        if num > mavVal: 
            mavVal = num

    print(mavVal)

#5. Calculate a remainder (given a numerator / denominator)

def calcRemainder(numerator, denominator): 
    #this seems too obvious??
    print(numerator % denominator)

    #how would you do this without using modulo??

#6. Return distinct values from a list including duplicates 

def distinctList(input_list):
    res = []

    for i in input_list:
        if i not in res:
            res.append(i)

    print(res)

    #how would you do this without using "in"? python makes this trivial
    #you could find the max value in the list and then create an array of
    #that size and simply add elements by index. This would be O(2n)?

#7. Return distinct values and their counts from a list 
# i.e. for [1, 1, 2, 3, 3, 3, 5] you would return "1(2) 2(1) 3(3) 5(1)"

#def distinctValuePairs(input_list):

#8. Given a string of expressions (+ and -) and a set of variables (a=1, b=7, etc.)
# return the return the result of the expression "a + b + c - d"

#def expressionString(expressions, variables):

if __name__=="__main__":
    # fizzBuzz(100)   
    # strReverse("Hello")
    # findMinVal([0, 4, 2, 9, -1])
    # findMaxVal([0, 4, 2, 9, -1])
    # calcRemainder(8, 6)
    distinctList([0, 4, 2, 9, -1, 0, 0, 4, -1, 12, -1, -1])