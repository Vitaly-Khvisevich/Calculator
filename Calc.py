from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Calculator')
root.geometry('300x220+500+200')

class Calc:
    def __init__(self):
        self.number=0
        self.number_temp=""
        self.operator=""
        self.f=Frame(root)
        self.f.pack(pady=10)
        self.e_display=Entry(self.f,bd=2, justify=RIGHT )
        self.e_display.grid(row=0,ipady=6, columnspan=6, sticky=N+S+W+E)
    
    def calc_actions(self, number1, number2, operator ):
        print(number1, number2, operator)
        actions = {
        "*": lambda x, y: str(float(x) * float(y)),
        "/": lambda x, y: str(float(x) / float(y)),
        "+": lambda x, y: str(float(x) + float(y)),
        "-": lambda x, y: str(float(x) - float(y))
        }
        for self.symbol, action in actions.items():
            if self.symbol == operator:
                s=action(number1, number2)
        return s
    
    def New_button(self, Name, b_row, b_column, b_rowspan=1, b_columnspan=1, b_sticky="") :
        self.button=Button(self.f, text=Name,padx=20, pady=9, command=lambda: self.out_monitor(Name))
        self.button.grid(rowspan=b_rowspan, columnspan=b_columnspan, row=b_row, column=b_column, sticky=b_sticky)  

    def out_monitor(self, name):
        numbers=['1','2','3','4','5','6','7','8','9','0','.']
        operators=['/', '*', '+', '-']
        if name in numbers:
            self.e_display.insert(END,name)
            self.number_temp=self.number_temp+name     
        elif name in operators:
            if self.operator=="":
                self.operator=name
                if self.number_temp !="":
                    self.number=float(self.number_temp)    
                else:
                    self.number=0
                    self.e_display.insert(END,0) 
                self.e_display.insert(END,name)
                self.number_temp=''
            else:
                self.number=self.calc_actions(self.number, float(self.number_temp), self.operator)
                self.e_display.insert(END,name)
                self.operator=name
                self.number_temp=''
        elif name =="<-":
            self.e_display.delete((len(self.e_display.get()))-1)
            self.number_temp=self.number_temp[0:-1]
        elif name =="=": 
            self.number=self.calc_actions(self.number, float(self.number_temp), self.operator)  
            self.e_display.delete(0,END)   
            self.e_display.insert(END,round(float(self.number),2))
            self.number=0
            self.number_temp=""
            self.operator=""
        elif name =="C": 
            self.e_display.delete(0,END)
            self.number=0
            self.number_temp=""
            self.operator=""   
        else:
            messagebox.showinfo("info", "Check the entered data")



y=Calc()
btn_lst =(
    '9','8','7','/',
    '6','5','4','*',
    '3','2','1','-',
    '0','.','+', "<-",
    "=","C"
)
row=1
column=0

for i in btn_lst:
    if i=='0':
        y.New_button(i,row, column,b_columnspan=2, b_sticky=N+S+W+E)
        column+=2
    elif i=="<-":
        y.New_button(i,2, 5, b_sticky=N+S+W+E)
    elif i=="C":
        y.New_button(i,1, 5, b_sticky=N+S+W+E)
    elif i=="=":
        y.New_button(i,3, 5,b_rowspan=2, b_sticky=N+S+W+E)
    else:
        y.New_button(i,row, column)
        column+=1
        if column==4:
            column=0
            row+=1




root.mainloop()