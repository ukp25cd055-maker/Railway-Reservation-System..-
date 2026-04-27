# Railway Reservation System

total_seats = 5
available_seats = list(range(1, total_seats + 1))
bookings = {}

def check_availability():
    print("Available seats:", available_seats)

def book_ticket():
    if not available_seats:
        print("No seats available!")
        return

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    seat = available_seats.pop(0)
    booking_id = len(bookings) + 1

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    print(f"Ticket booked! Booking ID: {booking_id}, Seat No: {seat}")

def view_ticket():
    booking_id = int(input("Enter booking ID: "))

    if booking_id in bookings:
        b = bookings[booking_id]
        print("Name:", b["name"])
        print("Age:", b["age"])
        print("Seat No:", b["seat"])
    else:
        print("Booking not found!")

def cancel_ticket():
    booking_id = int(input("Enter booking ID to cancel: "))

    if booking_id in bookings:
        seat = bookings[booking_id]["seat"]
        available_seats.append(seat)
        available_seats.sort()

        del bookings[booking_id]
        print("Ticket cancelled successfully!")
    else:
        print("Booking not found!")

# Menu
while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_availability()
    elif choice == 2:
        book_ticket()
    elif choice == 3:
        view_ticket()
    elif choice == 4:
        cancel_ticket()
    elif choice == 5:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
