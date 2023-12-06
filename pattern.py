print("Please enter the pattern to be printed")
ch = input()

if ch in ['a','e','i','o','u']:
    print("Vowels are not allowed")
else:
    if len(ch) > 1:
        print("the length of the character should not be greater than 1")
    else:
        for i in range(1,10,2):
            for j in range(i):
                print(ch , end = "") 
            print("")
                