import mysql.connector

def save_to_mysql(prompt):
    try:
        connection = mysql.connector.connect(
            host='your_mysql_host',
            user='your_mysql_user',
            password='your_mysql_password',
            database='your_database_name'
        )

        cursor = connection.cursor()

        # Insert the prompt into the 'history' table
        insert_query = "INSERT INTO history (prompt) VALUES (%s)"
        cursor.execute(insert_query, (prompt,))

        connection.commit()
        print("Prompt saved successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

# Example usage:
user_prompt = "Your user's input prompt"
save_to_mysql(user_prompt)
