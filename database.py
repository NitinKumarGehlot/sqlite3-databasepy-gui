import sqlite3

#create a database with table
def create_database_with_table():
    conn=sqlite3.connect("ourdata.db")
    c=conn.cursor()

    #create table
    c.execute("""CREATE TABLE users (
            first_name text,
            last_name text,
            email text
        ) """)
    #commit our command
    conn.commit()
    #close connection
    conn.close()



#add a new record to the table
def add_one(first,last,email):
    conn=sqlite3.connect("ourdata.db")
    c=conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)",(first,last,email))
    #commit our command
    conn.commit()
    #close our connection
    conn.close()



#add many record to the table
def add_many(list):
    conn=sqlite3.connect("ourdata.db")
    c=conn.cursor()
    c.executemany("INSERT INTO users VALUES (?,?,?)",(list))
    #commit our command
    conn.commit()
    #close our connection
    conn.close()




#Query The DB and return All records
def show_all():
    #connect to database and create cursor
    conn=sqlite3.connect("ourdata.db")
    c=conn.cursor()

    #query the database
    c.execute("SELECT rowid, * FROM users")
    item=c.fetchall()
    return(item)

    # for i in item:
    #     print(i)
    #commit our command
    conn.commit()
    #close our connection
    conn.close()



#delete record from table
def delete_one(id):
    conn=sqlite3.connect("ourdata.db")
    c=conn.cursor()

    c.execute("DELETE from users WHERE rowid=(?)",id)

    a=10
    #commit our command
    conn.commit()
    #close our connection
    conn.close()


def create_table():
    conn=sqlite3.connect("ourdata.db")
    c=conn.cursor()

    #create table
    c.execute("""CREATE TABLE employee (
            first_name text,
            last_name text,
            email text
        ) """)
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def create_database():
    conn=sqlite3.connect("newdata.db")
    c=conn.cursor()

    #commit our command
    conn.commit()
    #close connection
    conn.close()


