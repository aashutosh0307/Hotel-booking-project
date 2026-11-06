import os

# Room details dictionary
ROOMS = {
    "101": {"type": "Single", "rate": 2000},
    "102": {"type": "Double", "rate": 3500},
    "201": {"type": "Suite", "rate": 6000}
}

BOOKINGS_FILE = "bookings.txt"

def load_bookings():
    """Load bookings from bookings.txt into a list of dictionaries at program start."""
    bookings = []
    if os.path.exists(BOOKINGS_FILE):
        try:
            with open(BOOKINGS_FILE, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    # Expected format: Room101-Amit-2nights or flexible parsing
                    # Let's parse securely: "Room101-Amit-2nights" -> room="101", guest="Amit", nights=2
                    if line.startswith("Room"):
                        parts = line.replace("Room", "").split("-")
                        if len(parts) >= 3:
                            room_no = parts[0]
                            guest_name = parts[1]
                            nights_str = parts[2].replace("nights", "").replace("night", "").strip()
                            if nights_str.isdigit():
                                bookings.append({
                                    "room": room_no,
                                    "guest": guest_name,
                                    "nights": int(nights_str)
                                })
        except Exception as e:
            print(f"Error loading bookings: {e}")
    return bookings

def save_bookings(bookings):
    """Save current bookings list to bookings.txt after every change."""
    try:
        with open(BOOKINGS_FILE, "w") as file:
            for b in bookings:
                night_label = "night" if b["nights"] == 1 else "nights"
                file.write(f"Room{b['room']}-{b['guest']}-{b['nights']}{night_label}\n")
    except Exception as e:
        print(f"Error saving bookings: {e}")

def view_available_rooms(bookings):
    """View available rooms by filtering out currently booked rooms."""
    booked_rooms = [b["room"] for b in bookings]
    print("\n--- Available Rooms ---")
    available_found = False
    for room_no, details in ROOMS.items():
        if room_no not in booked_rooms:
            print(f"{room_no} {details['type']} Rs. {details['rate']}")
            available_found = True
    if not available_found:
        print("No rooms currently available.")
    print("-" * 23)

def book_room(bookings):
    """Book a room for a guest for 1 to 30 nights with validation and bill calculation."""
    print("\n--- Book a Room ---")
    guest = input("Enter Guest Name: ").strip()
    if not guest:
        print("Guest name cannot be empty.")
        return

    room_no = input("Enter Room Number (101, 102, 201): ").strip()
    if room_no not in ROOMS:
        print("Invalid room number. Please choose a valid room.")
        return

    # Check if already booked
    for b in bookings:
        if b["room"] == room_no:
            print(f"Room {room_no} is already booked by {b['guest']}. Please choose another room.")
            return

    try:
        nights = int(input("Enter Number of Nights (1 to 30): "))
        if nights < 1 or nights > 30:
            print("Invalid number of nights! Nights must be between 1 and 30.")
            return
    except ValueError:
        print("Please enter a valid integer for nights.")
        return

    # Calculate Bill = rate * nights + 12% GST
    rate = ROOMS[room_no]["rate"]
    base_amount = rate * nights
    gst = base_amount * 0.12
    total_bill = base_amount + gst

    # Add to bookings list
    bookings.append({
        "room": room_no,
        "guest": guest,
        "nights": nights
    })
    save_bookings(bookings)

    night_str = "night" if nights == 1 else "nights"
    print(f"\nRoom {room_no} booked for {guest} | {nights} {night_str}")
    print(f"Bill: {base_amount} + GST {int(gst) if gst.is_integer() else gst} = Rs. {int(total_bill) if total_bill.is_integer() else total_bill}")

def generate_bill(bookings):
    """Generate and display the bill for an active booking."""
    print("\n--- Generate Bill ---")
    room_no = input("Enter Room Number to generate bill: ").strip()
    
    target_booking = None
    for b in bookings:
        if b["room"] == room_no:
            target_booking = b
            break
            
    if not target_booking:
        print(f"No active booking found for Room {room_no}.")
        return

    rate = ROOMS[room_no]["rate"]
    nights = target_booking["nights"]
    base_amount = rate * nights
    gst = base_amount * 0.12
    total_bill = base_amount + gst

    print(f"\n--- Invoice ---")
    print(f"Guest Name : {target_booking['guest']}")
    print(f"Room Number: {room_no} ({ROOMS[room_no]['type']})")
    print(f"Nights     : {nights}")
    print(f"Rate/Night : Rs. {rate}")
    print(f"Base Amount: Rs. {base_amount}")
    print(f"GST (12%)  : Rs. {gst}")
    print(f"Total Bill : Rs. {total_bill}")
    print("-" * 15)

def cancel_booking(bookings):
    """Cancel an existing booking by room number."""
    print("\n--- Cancel Booking ---")
    room_no = input("Enter Room Number to cancel booking: ").strip()
    
    target_booking = None
    for b in bookings:
        if b["room"] == room_no:
            target_booking = b
            break
            
    if target_booking:
        bookings.remove(target_booking)
        save_bookings(bookings)
        print(f"Booking for room {room_no} cancelled. Room {room_no} is now available.")
    else:
        print(f"No active booking found for Room {room_no}.")

def main():
    bookings = load_bookings()
    
    while True:
        print("\n==============================")
        print(" HOTEL ROOM BOOKING SYSTEM")
        print("==============================")
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. Generate Bill")
        print("4. Cancel Booking")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            view_available_rooms(bookings)
        elif choice == '2':
            book_room(bookings)
        elif choice == '3':
            generate_bill(bookings)
        elif choice == '4':
            cancel_booking(bookings)
        elif choice == '5':
            print("Thank you for using Hotel Room Booking System. Goodbye!")
            break
        else: 
            print("Invalid choice! Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()#
