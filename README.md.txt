# Hotel Room Booking System (PS No. 69)

## Project Overview
The **Hotel Room Booking System** is a console-based Python application designed to manage hotel room inventory, guest bookings, cancellations, and bill generation. It features persistent data storage using text files so that booking records remain intact across program executions.

## Python Concepts Used
- **Dictionaries:** To store room inventory details (room number, type, and rates) and structure booking records.
- **Lists:** To manage the active list of bookings dynamically in memory.
- **Functions:** Modular code design separating core operations (`view_available_rooms`, `book_room`, `generate_bill`, `cancel_booking`, `load_bookings`, `save_bookings`).
- **File Handling:** Reading from and writing to `bookings.txt` to persist data after every change.

## Room Tariff Structure
- **101 Single:** Rs. 2,000 / night
- **102 Double:** Rs. 3,500 / night
- **201 Suite:** Rs. 6,000 / night
- **Tax:** 12% GST applied on the base room rent.
- **Stay Duration:** Validated between 1 to 30 nights.

## Features
1. **View Available Rooms:** Displays rooms that are currently not occupied.
2. **Book a Room:** Allows booking by entering guest name, room number, and number of nights with strict validation (no double-booking, range checks for nights).
3. **Generate Bill:** Computes base rate, 12% GST, and total payable amount.
4. **Cancel Booking:** Removes the booking from the system and frees up the room.
5. **File Persistence:** Automatically loads and updates `bookings.txt`.

## How to Run
1. Ensure Python 3 is installed on your system.
2. Place `one.py` and `bookings.txt` (optional, created automatically) in the same directory.
3. Run the application from your console/terminal:
   ```bash
   python3 one.py