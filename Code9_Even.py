#print 10 Even numbers
def Even(n):
    for i in range(1,n+1):
        print(i*2)
def main():
    n=input("Enter the number:-")
    Even(int(n))
if __name__=="__main__":
    main()