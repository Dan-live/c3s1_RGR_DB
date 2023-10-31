# ControllerClient
############################################################################
class ControllerClient:
    def __init__(self, model_client, view_client):
        self.model_client = model_client
        self.view_client = view_client

    def add_client(self):
        client_id = self.view_client.get_client_id()
        name, surname, email = self.view_client.get_client_input()
        if self.model_client.add_client(client_id, name, surname, email):
            self.view_client.show_client_message("Client added successfully!")
        else:
            self.view_client.show_client_message("Failed to add client.")

    def view_clients(self):
        clients = self.model_client.get_all_clients()
        self.view_client.show_clients(clients)

    def update_client(self):
        # Запрос ID бронирования, которое нужно обновить
        client_id = self.view_client.get_client_id()

        # Проверка, существует ли бронирование с указанным ID
        client_exists = self.model_client.check_client_existence(client_id)

        if client_exists:
            # Запрос обновленных данных о client от пользователя
            name, surname, email = self.view_client.get_client_input()
            # Вызов метода из класса Model для обновления client
            success = (self.model_client.update_client(client_id, name, surname, email))

            # Отображение сообщения о результате операции
            if success:
                self.view_client.show_client_message("Client updated successfully!")
            else:
                self.view_client.show_client_message("Failed to update client.")
        else:
            self.view_client.show_client_message("Client with the specified ID does not exist.")

    def delete_client(self):
        client_id = self.view_client.get_client_id()
        if self.model_client.delete_client(client_id):
            self.view_client.show_client_message("Client deleted successfully!")
        else:
            self.view_client.show_client_message("Failed to delete client.")
