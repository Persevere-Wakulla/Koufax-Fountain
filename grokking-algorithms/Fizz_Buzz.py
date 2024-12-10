def fizz_buzz():
    for n in range(100 + 1):
        output = ""
        if n % 3 == 0:
            output += "Fizz"
        if n % 5 == 0:
            output += "Buzz"
        print(output or n)
            
fizz_buzz()