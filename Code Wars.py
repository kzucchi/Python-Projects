#solutions for codewars challenges
#portfolio of python work

#Complete the function to multiply a with b

def multiply(a,b):
    return a * b

#Correct this code, so that the greet function returns the expected value:


class Person:
    def __init__(self, name):
      self.name = name
    def greet(self,other_name):
      return "Hi {0}, my name is {1}".format(other_name,self.name)

#Create a function named divisors that takes an integer
    #and returns an array with all of the integer's divisors(except for 1 and the number itself).
    #If the number is prime return the string '(integer) is prime' (use Either String a in Haskell).


def divisors(integer):
    divisible = []
    for i in range(2, integer):
        if integer % i == 0:
            divisible.append(i)
    if not divisible:
        return "{integer} is prime".format(integer=integer)
    else:
        return divisible


if __name__ == '__main__':
    print(divisors(15))
    print(divisors(12))


#best practices solution


    def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
