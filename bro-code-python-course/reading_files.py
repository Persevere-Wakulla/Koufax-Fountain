try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file is not found!")   
    
