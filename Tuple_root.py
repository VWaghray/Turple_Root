from tkinter import *
root = Tk()

root.geometry('800x400')
root.title('Sales Application')
root.config(bg = 'orange')
 
label = Label(root, fg = 'blue', bg = 'orange')
label1 = Label(root, fg = 'blue', bg = 'orange')
label2 = Label(root, fg = 'blue', bg = 'orange')
label3 = Label(root, fg = 'blue', bg = 'orange')

months = ('January','February','March','April','May','June','July','August','September','October','November','December')
Money = (50000, 65000, 100000, 75000, 76123, 386546, 90876, 99888, 99999, 12345, 78868,12345)

label["text"] = "Months: " + str(months)
label1["text"] = 'Profits: ' + str(Money)

def Profit_Max():
    Profit = max(Money)
    Profit_Index = Money.index(Profit)
    Monthss = months[Profit_Index]
    label2["text"] = "Maximum Profit is $" + str(Profit) +" and was given in the month of " + str(Monthss)
    

def Profit_Min():
    Loss = min(Money)
    Loss_Index = Money.index(Loss)
    Monthsss = months[Loss_Index]
    label3["text"] = "Minimum Profit is $" + str(Loss) +" and was given in the month of " + str(Monthsss)


btn = Button(root, text = "Show Max Profitable Month", command = Profit_Max, bg = "blue", fg = 'orange')
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn1 = Button(root, text = "Show Min Profitable Month", command = Profit_Min, bg = "blue", fg = 'orange')
btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
label.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label3.place(relx = 0.5, rely = 0.8, anchor = CENTER)


root.mainloop()