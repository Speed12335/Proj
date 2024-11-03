import pymysql.connector as mc
from mc import Error

password = ''

# Connect to the database
def connect():
    try:
        connection = mc.connect(host='localhost',user='root',passwd = password  )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"create database if not exists Atlas")
            connection.database = 'Atlas'
            print("Connected to database successfully!")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Initialize tables for hotel and bookings
def initialize_tables(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                room_id INT PRIMARY KEY AUTO_INCREMENT,
                room_number INT NOT NULL UNIQUE,
                room_type VARCHAR(20),
                price DECIMAL(10, 2),
                is_available BOOLEAN DEFAULT TRUE
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                booking_id INT PRIMARY KEY AUTO_INCREMENT,
                room_id INT,
                customer_name VARCHAR(100),
                check_in_date DATE,
                check_out_date DATE,
                FOREIGN KEY (room_id) REFERENCES rooms(room_id)
            )
        """)
        print("Tables initialized successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to add rooms to the database
def add_room(connection, room_number, room_type, price):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO rooms (room_number, room_type, price, is_available) 
            VALUES (%s, %s, %s, %s)
        """, (room_number, room_type, price, True))
        connection.commit()
        print(f"Room {room_number} added successfully.")
    except Error as e:
        print(f"Error: {e}")

# Function to check available rooms
def check_available_rooms(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM rooms WHERE is_available = TRUE")
        rooms = cursor.fetchall()
        if rooms:
            print("Available Rooms:")
            for room in rooms:
                print(f"Room ID: {room[0]}, Room Number: {room[1]}, Type: {room[2]}, Price: ${room[3]}")
        else:
            print("No rooms available.")
    except Error as e:
        print(f"Error: {e}")

# Function to book a room
def book_room(connection, room_id, customer_name, check_in_date, check_out_date):
    try:
        cursor = connection.cursor()
        
        # Check if the room is available
        cursor.execute("SELECT is_available FROM rooms WHERE room_id = %s", (room_id,))
        room = cursor.fetchone()
        if not room:
            print("Room not found.")
            return
        if not room[0]:  # room[0] is is_available
            print("Room is not available.")
            return
        
        # Book the room
        cursor.execute("""
            INSERT INTO bookings (room_id, customer_name, check_in_date, check_out_date) 
            VALUES (%s, %s, %s, %s)
        """, (room_id, customer_name, check_in_date, check_out_date))
        
        # Update room availability
        cursor.execute("UPDATE rooms SET is_available = FALSE WHERE room_id = %s", (room_id,))
        connection.commit()
        print(f"Room {room_id} booked successfully for {customer_name}.")
    except Error as e:
        print(f"Error: {e}")

# Function to view all bookings
def view_bookings(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT b.booking_id, r.room_number, b.customer_name, b.check_in_date, b.check_out_date 
            FROM bookings b
            JOIN rooms r ON b.room_id = r.room_id
        """)
        bookings = cursor.fetchall()
        if bookings:
            print("Bookings:")
            for booking in bookings:
                print(f"Booking ID: {booking[0]}, Room Number: {booking[1]}, Customer: {booking[2]}, "
                      f"Check-in: {booking[3]}, Check-out: {booking[4]}")
        else:
            print("No bookings found.")
    except Error as e:
        print(f"Error: {e}")

# Connect to the database
connection = connect()

# Initialize tables
initialize_tables(connection)

# Example usage
add_room(connection, room_number=101, room_type="Single", price=100)
add_room(connection, room_number=102, room_type="Double", price=150)
add_room(connection, room_number=103, room_type="Suite", price=250)

check_available_rooms(connection)

book_room(connection, room_id=1, customer_name="John Doe", check_in_date="2023-11-01", check_out_date="2023-11-05")

view_bookings(connection)

# Close the database connection
if connection.is_connected():
    connection.close()
    print("Connection closed.")
