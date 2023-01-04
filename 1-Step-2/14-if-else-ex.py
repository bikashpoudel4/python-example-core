"""Conditionals : if - else (Other Example) """

# example  if - else 

def main():
    a = input("Enter first number: ")
    b = input("Enter Second number: ")
    
    if int(b) == 0:
        print("Cannot be divide by 0")
    else:
        print("Dividing", a, "by", b)
        print(int(a)/int(b))
        
        # or
        # print("Dividing", a, "by", b)
        # div = int(a)/int(b)
        # print(div, "is answer")
        

main()