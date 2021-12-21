#check entered number is zero,positive,negative.

def Chknum(n):
    if(n==0):
        print("ZERO")
    elif(n>0):
        print("POSITIVE")
    else:
        print("NEGATIVE")
def main():
    n=input("Enter the number")
    Chknum(int(n))
if __name__=="__main__":
    main()
