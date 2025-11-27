from interfaces import Ticket

class TicketDecorator(Ticket):
    def __init__(self, wrapped_ticket):
        self.wrapped_ticket = wrapped_ticket

    def display_info(self):
        return self.wrapped_ticket.display_info()

    def attach(self, observer):
        self.wrapped_ticket.attach(observer)

    def resolve_ticket(self):
        self.wrapped_ticket.resolve_ticket()

class UrgentDecorator(TicketDecorator):

    def display_info(self):
        base_info = self.wrapped_ticket.display_info()
        return f"!!! URGENT !!! -> {base_info} <- !!! URGENT !!!"