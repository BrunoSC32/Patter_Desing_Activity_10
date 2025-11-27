from domain.interfaces import TicketRepository


class InMemoryTicketRepository(TicketRepository):
    def __init__(self):
        self._tickets = {}

    def save(self, ticket):
        self._tickets[ticket.ticket_id] = ticket
        return ticket

    def get(self, ticket_id):
        return self._tickets.get(ticket_id)

    def list_all(self):
        return list(self._tickets.values())
