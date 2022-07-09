import mysql.connector
 
# Connect to the database server using the provided credentials
# Note: user="root" for admin account
mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="ewis_student",
            passwd="ewis2020",
            database="company"
        )
# Open a cursor
mycursor = mydb.cursor(dictionary=True)
 
# Execute SQL query
mycursor.execute("SELECT * FROM employee")
 
# Get results from the query using the cursor
myresult = mycursor.fetchall()
 
# Close the cursor
mycursor.close()