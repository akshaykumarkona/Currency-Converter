with open('currency List.txt') as f1:
    all_lines=f1.readlines()

dict1={}
for i in all_lines:
    # print(i)
    a=i.split("\t")
    # print(a)
    dict1[a[0]]=a[1]
    # print(dict1)


def main_func():
    amt=int(input("Enter amount in INR:\n"))
    print(f"Enter the name of currency you want to convert this amount to? Available options are:\n")
    [print(j) for j in dict1.keys()]
    currency = input("Please enter one of these values:\n")
    print(f'{amt} INR is equal to {amt * float(dict1[currency])} {currency}')

main_func()
o=int(input("If you wish to convert currency once again enter 1 otherwise 0:  \n"))
while o>=0:
    if o==1:
        main_func()
    else:
        print("Thanks for using this project.")
        break


