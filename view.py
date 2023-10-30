# booking_ticket
#################################################################################
class ViewBookingTicket:

    def show_booking_tickets(self, booking_tickets):
        print("Booking Tickets:")
        for booking_ticket in booking_tickets:
            print(
                f"Booking ID: {booking_ticket[0]}, Client ID: {booking_ticket[1]}, Room Number: {booking_ticket[2]}, "
                f"Start Date: {booking_ticket[3]}, End Date: {booking_ticket[4]}, Price: {booking_ticket[5]}")

    def get_booking_ticket_input(self):
        client_id = int(input("Enter client ID: "))
        room_number = int(input("Enter room number: "))
        booking_start_date = input("Enter booking start date (YYYY-MM-DD): ")
        booking_end_date = input("Enter booking end date (YYYY-MM-DD): ")
        price = float(input("Enter booking price: "))
        return client_id, room_number, booking_start_date, booking_end_date, price

    def get_booking_id(self):
        return int(input("Enter booking ID: "))

    def show_booking_ticket_message(self, message):
        print(message)


# client
#################################################################################
class ViewClient:
    def show_clients(self, clients):
        print("Clients:")
        for client in clients:
            print(f"ID: {client[0]}, Name: {client[1]}, Surname: {client[2]}, Email: {client[3]}")

    def get_client_input(self):
        name = input("Enter client name: ")
        surname = input("Enter client surname: ")
        email = input("Enter client email: ")
        return name, surname, email

    def get_client_id(self):
        return int(input("Enter client id: "))

    def show_client_message(self, message):
        print(message)

# ViewRoom
#################################################################################


class ViewRoom:
    def show_rooms(self, rooms):
        print("Rooms:")
        for room in rooms:
            print(f"Room Number: {room[0]}, Room Type: {room[1]}")

    def get_room_input(self):
        room_type = input("Enter room type: ")
        return room_type

    def get_room_number(self):
        return int(input("Enter room number: "))

    def show_room_message(self, message):
        print(message)


class View:

    def show_tasks(self, tasks):
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}")

    def get_task_input(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        return title, description

    def get_task_id(self):
        return int(input("Enter task ID: "))

    def show_message(self, message):
        print(message)
