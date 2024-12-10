# infinite loop
# def countdown(i):
#     print(i)
#     countdown(i - 1)

# countdown(20)


def countdown(i):
    print(i)
    if i <= 0:  #Base case
        return
    else:       #Recursive case
        countdown(i - 1)

countdown(20)
