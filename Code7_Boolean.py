#number is divisible by 5 then print True otherwise false
def Boolean(n):
    if((n%5)==0):
        return True
    else:
        return False
def main():
    n=input("Enter the number:-")
    print(Boolean(int(n)))
if __name__=="__main__":
    main()
