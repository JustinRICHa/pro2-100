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


#del
def delete_user(connection, user_id:int):
    query = "DELETE FROM users WHERE id = ?"
    try:
        with connection:
            connection.execute(query,(user_id,))
            print(f"USER ID: {user_id} was deleted!")
    except Exception as e:
        print(e)


#update user
def update_user(connection, user_id:int, email:str):
    query = "UPDATE users SET email = ? WHERE id = ?"
    try:
        with connection:
            connection.execute(query,(email, user_id))
            print(f"User ID {user_id} has new email or {email} ")
    except Exception as e:
        print(e)

#add multiple users at the same time
def insert_users(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
    try:
        with connection:
            connection.executemany(query, users)
            print(f"{len(users)} users were added to the database!")
    except Exception as e:
        print(e)










def main():
    connection = get_connetion("subscribe.db")
    try:
    #create table
        create_table(connection)

        x= int(input("1 - activate, 2- freeze: "))
        while x != 2:



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

            elif start == "delete":
                user_id = int(input("Enter user ID: "))
                delete_user(connection, user_id)

            elif start == "update":
                user_id = int(input("Enter user ID: "))
                newemail = input("enter a new email: ")
                update_user(connection, user_id, newemail)

            elif start == "add many":
                users = [("jeb", 15,"kerbal@ksp.com"),
                        ("popeye", 106, "the_sailor@man.com"),
                        ("Guido", 70, "guido@youknow.org")]
                insert_users(connection, users)
            x= int(input("1 - activate, 2- freeze: "))
        
    finally:
        connection.close()


if __name__ == "__main__":
    main()

    ##2710