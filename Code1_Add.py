def Add(n1,n2):
    n3=int(n1)+int(n2)
    return n3

def main():
    n,m=input("Enter 2 numbers:-").split()
    #m=int(input("Enter 2nd number"))
    add=Add(n,m)
    print("addition of",n,"and",m,"is=",add)

if __name__=="__main__":
    main()