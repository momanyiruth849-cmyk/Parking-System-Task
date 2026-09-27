def main():
    slots = []
    for i in range(1, 21):
        slot = {
            "slot_number": i,
            "is_occupied": False,
            "vehicle_number": "",
            "check_in_time": 0,
            "name": ""
        }
        slots.append(slot)

    transactions = []

    choice = 0
    while choice != 5:
        print("\nWelcome to the Parking System")
        print("1. Sign in a vehicle")
        print("2. Check out a vehicle")
        print("3. View available parking slots")
        print("4. View revenue report")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            found_slot = False
            for slot in slots:
                if slot["is_occupied"] == False:
                    name = input("Enter your name: ")
                    plate = input("Enter your vehicle number plate: ")

                    try:
                        check_in_hour = int(input("Enter check-in hour (0-23): "))
                        check_in_minute = int(input("Enter check-in minute (0-59): "))
                    except ValueError:
                        print("Invalid input. Please enter numbers only.")
                        break

                    check_in_total = check_in_hour * 60 + check_in_minute

                    slot["is_occupied"] = True
                    slot["name"] = name
                    slot["vehicle_number"] = plate
                    slot["check_in_time"] = check_in_total

                    print("Slot", slot["slot_number"], "assigned to", name)
                    found_slot = True
                    break

            if found_slot == False:
                print("Sorry, no parking slots available.")

        elif choice == 2:
            plate = input("Enter vehicle number to check out: ")
            found_slot = False
            for slot in slots:
                if slot["vehicle_number"] == plate and slot["is_occupied"] == True:
                    try:
                        check_out_hour = int(input("Enter check-out hour (0-23): "))
                        check_out_minute = int(input("Enter check-out minute (0-59): "))
                    except ValueError:
                        print("Invalid input. Please enter numbers only.")
                        break

                    check_out_total = check_out_hour * 60 + check_out_minute
                    check_in_total = slot["check_in_time"]

                    duration_minutes = check_out_total - check_in_total
                    if duration_minutes < 0:
                        duration_minutes = duration_minutes + (24 * 60)

                    duration_hours = duration_minutes / 60

                    if duration_minutes <= 30:
                        fee = 0
                    elif duration_minutes <= 120:
                        fee = 50
                    elif duration_minutes <= 240:
                        fee = 100
                    elif duration_minutes <= 360:
                        fee = 300
                    else:
                        fee = 500

                    print("Vehicle", plate, "parked for", round(duration_hours, 2), "hour(s)")
                    print("Amount payable: KES", fee)
                    print("Barrier opening... Goodbye!")

                    transactions.append({
                        "plate": plate,
                        "name": slot["name"],
                        "hours": round(duration_hours, 2),
                        "fee": fee
                    })

                    slot["is_occupied"] = False
                    slot["vehicle_number"] = ""
                    slot["check_in_time"] = 0
                    slot["name"] = ""

                    found_slot = True
                    break

            if found_slot == False:
                print("Vehicle not found. Please check your plate number.")

        elif choice == 3:
            available_count = 0
            for slot in slots:
                if slot["is_occupied"] == False:
                    available_count = available_count + 1
            print("Total available slots:", available_count, "out of 20")

        elif choice == 4:
            admin_password = input("Enter admin password: ")
            if admin_password == "admin123":
                print("Access granted. Generating revenue report...")
                print("--- Revenue Report ---")
                if len(transactions) == 0:
                    print("No transactions yet.")
                else:
                    total_revenue = 0
                    for record in transactions:
                        print(record["plate"], "-", record["hours"], "hrs - KES", record["fee"])
                        total_revenue = total_revenue + record["fee"]
                    print("Total collected: KES", total_revenue)
            else:
                print("Access denied. Incorrect password.")

        elif choice == 5:
            print("Exiting the Parking System. Goodbye!")

        else:
            print("Invalid choice. Please try again.")

main()