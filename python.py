import pandas as pd
class Employee_Data:
    def createdata(self):
        data = {'Employee ID': ['161E90', '161F91', '161F99', '171E20', '171G30'],
                'Name': ['Raman', 'Himadri', 'Jaya', 'Tejas', 'Ajay'],
                'Age': [41, 38, 51, 30, 45],
                'Salary (PM)': [56000, 67500, 82100, 55000, 44000]
                }
        global df
        df = pd.DataFrame(data)
        print("Data Frame(Table) Created !!")
    def searchdata(self,ch,df):
        if(ch==1):
            age=int(input("Enter the desired age:"))
            print(df[df["Age"]==age])
        elif(ch==2):
            name=input("Enter the name you want to store:")
            print(df[df['Name']==name])
        elif(ch==3):
            sal=int(input("Enter the salary: (>, <, <=, >=)"))
            sym=input("Enter the symbol ")
            # print(df[df["Salary"] sym sal])
        else:
            print("Entered the wrong choice")
obj1=Employee_Data()
obj1.createdata()
while(True):
    print("Enter 1 for age.\n Enter 2 for Name.\n Enter 3 for salary.\nEnter 4 for exit:")
    ch=int(input())
    if(ch!=4):
        obj1.searchdata(ch,df)
    else:
        break





