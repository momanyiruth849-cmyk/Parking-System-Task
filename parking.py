"""
Modern Parking System - DSA Task 1
Simple console prototype that demonstrates the data structures and algorithms.
"""

from datetime import datetime

# =========================================================
# DATA STRUCTURES
# =========================================================

# 1. List of dictionaries – all parking bays
slots = []

# 2. Dictionary – active sessions (key = number plate)
active_sessions = {}

# 3. Simple list acting as free-bays queue
free_bays = []

# Parking rate (KES per hour) – can be changed easily
RATE_PER_HOUR = 100


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def initialize_slots(total_slots=20):
    """Create all parking bays and mark them as free."""
    global slots, free_bays
    slots = []
    free_bays = []

    for i in range(1, total_slots + 1):
        bay = {
            "slot_id": i,
            "status": "Free",
            "zone": "A" if i <= 10 else "B"
        }
        slots.append(bay)
        free_bays.append(i)

    print(f"System initialized with {total_slots} parking slots.")


def allocate_slot():
    """Return the next free bay ID, or None if full."""
    if not free_bays:
        return None
    return free_bays.pop(0)          # simple FIFO allocation


def find_slot(slot_id):
    """Find a slot dictionary by its ID."""
    for slot in slots:
        if slot["slot_id"] == slot_id:
            return slot
    return None


# =========================================================
# MAIN MODULES
# =========================================================

def process_arrival(number_plate):
    """Record a vehicle on arrival and allocate a bay."""
    number_plate = number_plate.strip().upper()

    if not number_plate:
        print("Invalid number plate.")
        return

    if number_plate in active_sessions:
        print("This vehicle is already parked.")
        return

    bay_id = allocate_slot()
    if bay_id is None:
        print("Sorry, the parking is full.")
        return

    # Mark bay as occupied
    slot = find_slot(bay_id)
    slot["status"] = "Occupied"

    # Create session
    entry_time = datetime.now()
    session = {
        "number_plate": number_plate,
        "slot_id": bay_id,
        "entry_time": entry_time,
        "status": "Active"
    }
    active_sessions[number_plate] = session

    print(f"\nVehicle {number_plate} checked in successfully.")
    print(f"Allocated Bay : {bay_id}")
    print(f"Entry Time    : {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Please proceed to the bay.\n")


def calculate_fee(number_plate):
    """Calculate duration and fee for a vehicle."""
    session = active_sessions.get(number_plate)
    if not session:
        return None

    exit_time = datetime.now()
    duration = exit_time - session["entry_time"]
    minutes = duration.total_seconds() / 60
    hours = minutes / 60

    # Charge at least 1 hour if less than 1 hour
    billable_hours = max(1, round(hours + 0.49))   # simple rounding up
    fee = billable_hours * RATE_PER_HOUR

    return {
        "exit_time": exit_time,
        "duration_minutes": int(minutes),
        "billable_hours": billable_hours,
        "fee": fee
    }


def process_exit(number_plate):
    """Calculate fee, collect payment (simulated), and free the bay."""
    number_plate = number_plate.strip().upper()

    if number_plate not in active_sessions:
        print("No active session found for this vehicle.")
        return

    result = calculate_fee(number_plate)
    if not result:
        return

    session = active_sessions[number_plate]

    print(f"\n----- Exit Summary -----")
    print(f"Vehicle       : {number_plate}")
    print(f"Bay           : {session['slot_id']}")
    print(f"Entry Time    : {session['entry_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Exit Time     : {result['exit_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Duration      : {result['duration_minutes']} minutes")
    print(f"Billable Hours: {result['billable_hours']}")
    print(f"Amount Due    : KES {result['fee']}")
    print("------------------------")

    # Simulate payment confirmation
    payment = input("Enter payment method (M-Pesa / Card / Cash): ").strip().title()
    if payment not in ["M-Pesa", "Card", "Cash"]:
        payment = "Cash"

    print(f"Payment of KES {result['fee']} received via {payment}.")
    print("Barrier opened. Thank you!\n")

    # Free the bay
    bay_id = session["slot_id"]
    slot = find_slot(bay_id)
    slot["status"] = "Free"
    free_bays.append(bay_id)
    free_bays.sort()               # keep the list tidy

    # Remove session
    del active_sessions[number_plate]


def show_available_slots():
    """Display how many slots are free and list them."""
    free_count = len(free_bays)
    total = len(slots)

    print(f"\nAvailable slots: {free_count} out of {total}")
    if free_count > 0:
        print("Free bays:", ", ".join(str(b) for b in free_bays))
    print()


def show_parked_vehicles():
    """Show all currently parked vehicles (extra useful feature)."""
    if not active_sessions:
        print("\nNo vehicles currently parked.\n")
        return

    print("\nCurrently Parked Vehicles:")
    print("-" * 50)
    for plate, session in active_sessions.items():
        print(f"{plate:12} | Bay {session['slot_id']:2} | Entered: {session['entry_time'].strftime('%H:%M:%S')}")
    print("-" * 50 + "\n")


# =========================================================
# MAIN MENU
# =========================================================

def main():
    initialize_slots(20)

    while True:
        print("=" * 40)
        print("   MODERN PARKING SYSTEM")
        print("=" * 40)
        print("1. Sign in a vehicle (Arrival)")
        print("2. Check out a vehicle (Exit)")
        print("3. View available parking slots")
        print("4. View currently parked vehicles")
        print("5. Exit system")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            plate = input("Enter vehicle number plate: ")
            process_arrival(plate)

        elif choice == "2":
            plate = input("Enter vehicle number plate to check out: ")
            process_exit(plate)

        elif choice == "3":
            show_available_slots()

        elif choice == "4":
            show_parked_vehicles()

        elif choice == "5":
            print("\nThank you for using the Parking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
