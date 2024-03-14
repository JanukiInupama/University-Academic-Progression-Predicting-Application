# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Student ID: W1956357/20221301
#Date:14.12.2022
# Part 4 
total = 0
Option = 'y'
dic = {}
while True:
    if Option== 'y':
        try:
            ID_num = input('Enter UOW ID number: ')
            if len(ID_num)==8:
                while True:
                    Pass_credit = int(input('Enter the pass credit: '))
                    if Pass_credit not in range(0,121,20):
                        print('Out of range')
                    else:
                        break
                while True:
                    Defer_credit = int(input('Enter the defer credit: '))
                    if Defer_credit not in range(0,121,20):
                        print('Out of range')
                    else:
                        break
                while True:
                    Fail_credit = int(input('Enter the fail credit: '))
                    if Fail_credit not in range(0,121,20):
                        print('Out of range')
                    else:
                        break
            else:
                print('Invalid input')
            total=Pass_credit+Defer_credit+Fail_credit
            if Pass_credit == 120:
                dic[ID_num]={}
                dic[ID_num]="Progress :",Pass_credit,Defer_credit,Fail_credit
            elif Pass_credit == 100:
                 dic[ID_num]={}
                 dic[ID_num]="Progress(module trailer) :",Pass_credit,Defer_credit,Fail_credit 
            elif Pass_credit == 40 and Defer_credit == 0:
                dic[ID_num]={}
                dic[ID_num]="Exclude :",Pass_credit,Defer_credit,Fail_credit
            elif Pass_credit == 20 and Defer_credit == 20 and 0:
                dic[ID_num]={}
                dic[ID_num]="Exclude :",Pass_credit,Defer_credit,Fail_credit
            elif Pass_credit == 0 and Defer_credit == 40 and 20 and 0:
                dic[ID_num]={}
                dic[ID_num]="Exclude :",Pass_credit,Defer_credit,Fail_credit
            else:
                if total!=120:
                    print('Out of range')
                else:
                    dic[ID_num]={}
                    dic[ID_num]="Progress(module retriever) :",Pass_credit,Defer_credit,Fail_credit
        except ValueError:
            print('Integer required')
        if total != 120:
            print('Total incorrect')
    elif Option == 'q':
        print('Quit the program.')
        break
    else:
        print('Invalid input')
        print('Would you like to enter another set of data?')
    Option=input("Enter 'y' for yes or 'q' to quit and view results: ")
print(dic)

                                                                                          
