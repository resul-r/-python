"""FizzBuzz Algorithm

If the integer (x) is divisible by 3, the output must be replaced by “Fizz”.
If the integer (x) is divisible by 5, the output must be replaced by “Buzz”.
If the integer (x) is divisible by 3 and 5, the output should be replaced by “FizzBuzz”. """



def funfizzbuzz(n):
    try:
        if(0<= n <= 100):
            for x in range(n):
                if x==0:
                    print("0")
                elif (x%3==0 and x%5==0) :
                    print("fizzbuzz")
                elif x%3==0:
                    print("fizz")
                elif x%5==0:
                    print("buzz")
                else:
                    print(x)    
    except Exception:
        print("ATTENTION!!! The number you entered was not in between 0 and 99 ")   

try:
    a = int(input("Please enter a number in between 0 and 99: "))
    funfizzbuzz(a)
except Exception:
    print(" ATTENTION!!!  Something went wrong here. Next time, try to enter a valid Integer ")



   


