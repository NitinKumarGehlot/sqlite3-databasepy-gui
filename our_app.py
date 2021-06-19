from tkinter import *
from tkinter import ttk
import database

root=Tk()
root.title("IOTtech")
root.geometry("600x600")


def fetch():
    data=database.show_all()
    li(data)
    


b2=Button(root,width=20,height=2,fg="white",bg="dark sea green",activebackground="peach puff",text="fetch data",font=("Calibri"),command=fetch)
b2.place(x=10,y=20)

listbox=Listbox(root,height=8,width=50)
listbox.place(x=30,y=100)
def li(a):
    listbox.delete(0,'end')
    l=1
    for i in a:
        listbox.insert(i[0],(l,i[1]))
        l+=1 
# database.create_database_with_table()



# database.add_one("Seema","Arya","seema@gmail.com")



# stuff = [
#     ('Upasana', 'Thakur', 'upasana@gmail.com'),
#     ('Hiteshi', 'Vashney', 'hittu@gmail.com')
#     ]
# database.add_many(stuff)









##important-- delete record use rowid as string
# database.delete_one('5')

# database.create_table()

# database.create_database()

root.mainloop()