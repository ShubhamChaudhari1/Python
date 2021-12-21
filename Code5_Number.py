#display 1 to 10 and 10 to 1 numbers
#There are three ways you can call range() : 
#range(stop) takes one argument.
#range(start, stop) takes two arguments.
#range(start, stop, step) takes three arguments.

def Number():
    for i in range(1,11):
        print(i," ")
    for n in range(10,0,-1):
        print(n," ")

def main():
    Number()

if __name__=="__main__":
    main()
