from interfaces import Ticket, Observer

class ITUser(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f" >> Notification for {self.name}: {message}")


class NetworkTicket(Ticket):
    def display_info(self):
        return f"Ticket #{self.ticket_id} [NETWORK]: {self.description}"

class SoftwareTicket(Ticket):
    def display_info(self):
        return f"Ticket #{self.ticket_id} [SOFTWARE]: {self.description}"