# ControllerBooking
############################################################################
class ControllerAnalytics:
    def __init__(self, model_analytics, view_analytics):
        self.model_analytics = model_analytics
        self.view_analytics = view_analytics

    def room_occupancy(self):
        # Отримати аналітичні дані
        room_occupancy_data = self.model_analytics.room_occupancy()

        # Вивести результати
        if room_occupancy_data:
            self.view_analytics.display_room_occupancy(room_occupancy_data)
        else:
            print("Помилка при виконанні аналітики")

    def number_of_orders(self):
        # Виконати аналітику
        number_of_orders_data = self.model_analytics.number_of_orders()

        # Вивести результати
        if number_of_orders_data:
            self.view_analytics.display_number_of_orders(number_of_orders_data)
        else:
            print("Помилка при виконанні аналітики зайнятості номерів")

    def client_analytics(self):
        # Виконати аналітику
        client_analytics_data = self.model_analytics.client_analytics()

        # Вивести результати
        if client_analytics_data is not None:
            self.view_analytics.display_client_analytics(client_analytics_data)
        else:
            print("Помилка при виконанні аналітики")