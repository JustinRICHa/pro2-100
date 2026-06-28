import sqlite3
#int
def get_connetion(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"error: {e}")
        raise


#table
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id  INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )

    """
    try:
        with connection:
            connection.execute(query)
            print("Table was created!")
    except Exception as e:
        print(e)

#add user

def insert_user(connection, name:str,  age:int, email:str):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
    try:
        with connection:
            connection.execute(query,(name, age, email))
            print(f"user: {name} was added to your databace")
    except Exception as e:
        print(e)


#query all users in DB
def fetch_users(connection, condition: str = None) -> list[tuple]: 
    
    query = "SELECT * FROM users"
    if condition:
        query += f"WHERE {condition}"


    try:
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    except Exception as e:
        print(e)





def main():
    connection = get_connetion("subscribe.db")
    try:
    #create table
        create_table(connection)

        start = input("enter option: (add, delete, update, search, add Many):").lower()
        if start == "add":
            name = input("enter name: ")
            age = int(input("enter age: "))
            email = input("enter email: ")
            insert_user(connection, name, age, email)
        elif start == "search":
            print("all users: ")
            for user in fetch_users(connection):
                print(user)
    finally:
        connection.close()


if __name__ == "__main__":
    main()

    ##2710