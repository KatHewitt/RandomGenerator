import pandas as pd
import random 
from tkinter import *

names = pd.read_csv('names.csv')
#print(names)
df = pd.DataFrame(names)
#print(df)
list = df['name'].tolist()
#print(list)
#print(random.choice(list))
#new = random.sample(list, 3)
#print(new)

name1 = (random.choice(list))
name2 = (random.choice(list))
name3 = (random.choice(list))

window = Tk()
lbl = Label(window, text = (name1 + '\n' + name2 +'\n'+ name3), fg='black', font=('Helvetica', 16))
lbl.place(x=60, y=50)
window.title('Random Name Selector')
window.geometry('300x200+10+20')
window.mainloop()

