# ----------------------------------
# if __name__ == "__main__"
# ----------------------------------

# y this?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if its the initial module being run

def main():
    print("Hello")
    
if __name__ == '__main__':
    main()

