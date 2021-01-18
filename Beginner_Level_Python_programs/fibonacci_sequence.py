#Fibonacci sequence starts with 0 and 1 as the first numbers and the consequetive numbers are calculated by adding up the two numbers before them
#0, 1, 1, 2, 3, 5, 8, 13 ...

# Function to claculate list of fibonacci numbers
def fibonacci_calc(num):
    result = list()
    count = 0 
    # Invalid input
    if num <= 0:
        print("Please enter a positive integer (input>0)")
        return result
    # Input 1
    elif num == 1:
        result.append(0)
        return result
    else:
        #starting values
        n1, n2 = 0, 1
        while count < num:
            result.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    return result


if __name__ == "__main__":
    fibo_list = list()
    n = int(input("Please enter the sequence number: "))
    fibo_list = fibonacci_calc(n)
    for i in fibo_list:
        print(i)
