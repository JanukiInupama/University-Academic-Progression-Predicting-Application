# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.   
# Student ID: W1956357/20221301
#Date: 14.12.2022
# Part 1,2 and 3 
total = 0
Option='y'
outcome = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
List_1=[]
while True:
    if Option== 'y':
        try:
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
            total=Pass_credit+Defer_credit+Fail_credit
            if Pass_credit == 120:
                print('Progress')
                List_1.append('Progress'+' '+'-'+' '+str(Pass_credit)+','+' '+str(Defer_credit)+','+' '+str(Fail_credit))
                progress = progress + 1
            elif Pass_credit == 100:
                print('Progress(module trailer)')
                List_1.append('Progress(module trailer)'+' '+'-'+' '+str(Pass_credit)+','+' '+str(Defer_credit)+','+' '+str(Fail_credit))
                trailer = trailer + 1
            elif Pass_credit == 40 and Defer_credit == 0:
                print('Exclude')
                List_1.append('Exclude'+' '+'-'+' '+str(Pass_credit)+','+' '+str(Defer_credit)+','+' '+str(Fail_credit))
                exclude = exclude + 1
            elif Pass_credit == 20 and Defer_credit == 20 and 0:
                print('Exclude')
                List_1.append('Exclude'+' '+'-'+' '+str(Pass_credit)+','+' '+str(Defer_credit)+','+' '+str(Fail_credit))
                exclude = exclude + 1
            elif Pass_credit == 0 and Defer_credit == 40 and 20 and 0:
                print('Exclude')
                List_1.append('Exclude'+' '+'-'+' '+str(Pass_credit)+','+' '+str(Defer_credit)+','+' '+str(Fail_credit))
                exclude = exclude + 1
            else:
                if total!=120:
                    print('Out of range')
                else:
                    print('Do not progress-module retriever')
                    List_1.append('Module retriever'+' '+'-'+' '+str(Pass_credit)+','+' '+str(Defer_credit)+','+' '+str(Fail_credit))
                    retriever = retriever + 1
            outcome = progress + trailer + retriever + exclude
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
print('-'*100)
print('Histogram')                                                                   #Histogram
print('Progress',progress,':','*'*progress,'\n'
      'Trailer',trailer,':','*'*trailer,'\n'
      'Retriever',retriever,':','*'*retriever,'\n'
      'Excluded',exclude,':','*'*exclude,'\n')
print(outcome,'outcomes in total')
print('-'*100)
for x in List_1:
    print(*List_1, sep="\n")
    break
file=open('myfile.txt','w')          #Part 3-Text file.
for x in range(len(List_1)):
    file.write(List_1[x])
    file.write('\n')
file.close()
 



