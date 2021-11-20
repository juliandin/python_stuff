import sqlite3


def database():
    """
    SQLite database creation / opening
    """
    global cursor
    global conn
    conn = sqlite3.connect('DINERS.db')
    cursor = conn.cursor()
    print("Successfully opened/created database.")


def dropAllData():
    """
    Deletes existing tables in order to create new ones.
    (Could not find a way to delete multiple tables with one statement. Seems like SQLite does not allow it.
    from SQLite documentation : "To remove multiple tables, you need to issue multiple DROP TABLE statements" :c)
    """
    cursor.execute("DROP TABLE CANTEEN;")
    cursor.execute("DROP TABLE PROVIDER;")


def createTables():
    """
    Creates necessary tables (canteens and providers) for Homework 2.
    """
    cursor.execute('''CREATE TABLE CANTEEN 
             (ID INT PRIMARY KEY NOT NULL,
              ProviderID INT NOT NULL,
              Name VARCHAR(40) NOT NULL,
              Location VARCHAR(50),
              time_open TIME,
              time_closed TIME,
              FOREIGN KEY (ProviderID)
              REFERENCES PROVIDER (ID));''')

    cursor.execute('''CREATE TABLE PROVIDER 
              (ID INT PRIMARY KEY NOT NULL,
              ProviderName VARCHAR(40) NOT NULL);''')

    print("Successfully added tables.")


def addRecords():
    """
    Adds all the necessary data into the tables.
    Data is taken from Homework 2 Moodle page.
    """
    sql_providers = """INSERT INTO PROVIDER(ID, ProviderName) VALUES (1, 'Rahva Toit'), 
    (2, 'Baltic Restaurants Estonia AS'), (3, 'TTÜ Sport OÜ'), (4, 'bitStop Kohvik OÜ');"""
    cursor.execute(sql_providers)

    sql_canteens = """INSERT INTO CANTEEN(ID, Name, Location, ProviderID, time_open, time_closed) VALUES 
    (1, "Economics- and social science building canteen", "Akadeemia tee 3 SOC- building", 1, "08:30", "18:30"),
    (2, "Library canteen", "Akadeemia tee 1/Ehitajate tee 7", 1, "08:30", "19:00"),
    (3, "Main building Deli cafe", "Ehitajate tee 5 U01 building", 2, "09:00", "16:30"),
    (4, "Main building Daily lunch restaurant", "Ehitajate tee 5 U01 building", 2, "09:00", "16:30"),
    (5, "U06 building canteen", "Ehitajate tee 5 U06 Building", 1, "09:00", "16:00"),
    (6, "Natural Science building canteen", "Akadeemia tee 15 SCI building", 2, "09:00", "16:00"),
    (7, "ICT building canteen", "Raja 15/Mäepealse 1", 2, "09:00", "16:00"),
    (8, "Sports building canteen", "Manniliiva 7 S01 building", 3, "11:00", "20:00");"""
    cursor.execute(sql_canteens)

    sql_it_college_canteen = """INSERT INTO CANTEEN(ID, ProviderID, Name, Location, time_open, time_closed) VALUES
    (9, 4, "bitStop KOHVIK", "IT College, Raja 4c", "9:30", "16:00");"""
    cursor.execute(sql_it_college_canteen)

    conn.commit()  # save changes
    print("Successfully inserted all data.")


def getRecords16_18():
    """
    Prints canteens that are open from 16.15 to 18.00.
    """
    sql_select_hw2 = """SELECT Name, Location, time_open, time_closed FROM CANTEEN, PROVIDER WHERE CANTEEN.ProviderID =
    PROVIDER.ID AND time_open <="16:15" AND time_closed >= "18:00";"""
    cursor.execute(sql_select_hw2)
    print('\n' + "Canteens that are open 16.15 - 18.00:")
    for row in cursor:
        print('Place: %s, Address %s, Open from %s until %s' % (row[0], row[1], row[2], row[3]))


def getRecordsRahvaToit():
    """
    Prints all canteens that are served by Rahva toit.
    """
    sql_select_hw2 = """SELECT Name, Location, ProviderName FROM CANTEEN, PROVIDER WHERE 
    CANTEEN.ProviderID = PROVIDER.ID AND PROVIDER.ProviderName = "Rahva Toit";"""
    cursor.execute(sql_select_hw2)
    print('\n' + "Places served by Rahva Toit:")
    for row in cursor:
        print('Place: %s, Address: %s, Service provider: %s' % (row[0], row[1], row[2]))


if __name__ == "__main__":
    database()  # creates new database or connects to an existing one
    dropAllData()  # deletes old 'canteen' and 'provider' tables and data if it is there
    createTables()  # adds 'canteen' and 'provider' tables
    addRecords()  # adds records into tables
    getRecords16_18()  # prints out canteens that are open from 16.15 to 18.00
    getRecordsRahvaToit()  # prints out canteens that are served by 'Rahva toit'
