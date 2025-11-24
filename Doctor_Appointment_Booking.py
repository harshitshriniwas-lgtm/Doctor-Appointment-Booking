# Simple Doctor Appointment Booking - Friendly Console Version

appointments = []
next_id = 1

def create_appointment():
    global next_id
    print("Let's book an appointment!")
    doctor = input("Doctor's name? ")
    patient = input("Patient's name? ")
    date_time = input("Date and time for the appointment? ")
    appointments.append({
        "id": next_id,
        "doctor": doctor,
        "patient": patient,
        "date_time": date_time
    })
    print(f"Appointment #{next_id} booked. Don't forget!")
    next_id += 1

def read_appointments():
    if not appointments:
        print("No appointments yet. Feel free to add one!")
    else:
        print("\n--- All Appointments ---")
        for app in appointments:
            print(f"(ID {app['id']}): Dr. {app['doctor']} has an appointment with {app['patient']} on {app['date_time']}.")

def update_appointment():
    try:
        id_to_update = int(input("What's the ID of the appointment to change? "))
    except ValueError:
        print("Please type a whole number for the appointment ID.")
        return

    found = False
    for app in appointments:
        if app['id'] == id_to_update:
            print("Leave blank if you don't want to change a field.")
            temp = input("New doctor's name? ")
            if temp: app['doctor'] = temp
            temp = input("New patient's name? ")
            if temp: app['patient'] = temp
            temp = input("New date and time? ")
            if temp: app['date_time'] = temp
            print("Updated! Hope that's correct.")
            found = True
            break
    if not found:
        print("Sorry, couldn't find that appointment.")

def delete_appointment():
    try:
        id_to_delete = int(input("Enter the ID to remove that appointment: "))
    except ValueError:
        print("A number, please!")
        return

    for i, app in enumerate(appointments):
        if app['id'] == id_to_delete:
            print(f"Removed appointment #{id_to_delete}.")
            appointments.pop(i)
            return
    print("No appointment found with that ID.")

while True:
    print("\nDoctor Appointment Menu")
    print("1. Book an appointment")
    print("2. Show all appointments")
    print("3. Change an appointment")
    print("4. Cancel an appointment")
    print("5. Quit")

    pick = input("What would you like to do? (1-5): ")
    if pick == "1":
        create_appointment()
    elif pick == "2":
        read_appointments()
    elif pick == "3":
        update_appointment()
    elif pick == "4":
        delete_appointment()
    elif pick == "5":
        print("See you next time!")
        break
    else:
        print("Hmm, that's not a valid menu option. Try a number from 1 to 5.")
