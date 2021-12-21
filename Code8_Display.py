#Display n times of * in line
def Display(n):
    for i in range(n):
        print("*",end=" ")
def main():
    n=input("Enter number:-")
    Display(int(n))
if __name__=="__main__":
    main()
