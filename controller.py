from model import Model

from Task.view import TaskView
from Task.model import ModelTask
from Task.controller import ControllerTask

from Booking.view import ViewBookingTicket
from Booking.model import ModelBookingTicket
from Booking.controller import ControllerBooking

from Client.view import ViewClient
from Client.model import ModelClient
from Client.controller import ControllerClient

from Room.view import ViewRoom
from Room.model import ModelRoom
from Room.controller import ControllerRoom


class Controller:
    def __init__(self):
        self.model = Model()
        self.view_task = TaskView()
        self.view_booking_ticket = ViewBookingTicket()
        self.view_client = ViewClient()
        self.view_room = ViewRoom()

        self.model_booking_ticket = ModelBookingTicket(self.model)
        self.model_client = ModelClient(self.model)
        self.model_room = ModelRoom(self.model)
        self.model_task = ModelTask(self.model)


        self.controller_booking = ControllerBooking(self.model_booking_ticket, self.view_booking_ticket)
        self.controller_client = ControllerClient(self.model_client, self.view_client)
        self.controller_room = ControllerRoom(self.model_room, self.view_room)
        self.controller_task = ControllerTask(self.model_task, self.view_task)

    def run(self):
        methods = {'1': self.controller_task.add_task, '2': self.controller_task.view_tasks,
                   '3': self.controller_task.update_task, '4': self.controller_task.delete_task,
                   '5': self.controller_booking.add_booking_ticket,
                   '6': self.controller_booking.view_booking_tickets,
                   '7': self.controller_booking.update_booking_ticket,
                   '8': self.controller_booking.delete_booking_ticket,
                   '9': self.controller_client.add_client, '10': self.controller_client.view_clients,
                   '11': self.controller_client.update_client, '12': self.controller_client.delete_client,
                   '13': self.controller_room.add_room, '14': self.controller_room.view_rooms,
                   '15': self.controller_room.update_room, '16': self.controller_room.delete_room}

        while True:
            choice = self.show_menu()

            if choice in methods:
                methods[choice]()
            elif choice == '17':
                break

    MENU_OPTIONS = [
        "Add Task",
        "View Tasks",
        "Update Task",
        "Delete Task",
        "Add Booking Ticket",
        "View Booking Tickets",
        "Update Booking Ticket",
        "Delete Booking Ticket",
        "Add Client",
        "View Clients",
        "Update Client",
        "Delete Client",
        "Add Room",
        "View Rooms",
        "Update Room",
        "Delete Room",
        "Quit"
    ]

    def show_menu(self):
        self.view_task.show_message("\nMenu:")
        for idx, option in enumerate(self.MENU_OPTIONS, start=1):
            self.view_task.show_message(f"{idx}. {option}")
        return input("Enter your choice: ")
