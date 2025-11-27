from .decorators import UrgentDecorator
from .factories import TicketFactory
from .interfaces import TicketRepository


class TicketService:
    def __init__(self, repository: TicketRepository):
        self._repository = repository

    def create_ticket(self, ticket_type, ticket_id, description, urgent=False):
        ticket = TicketFactory.create_ticket(ticket_type, ticket_id, description)
        if urgent:
            ticket = UrgentDecorator(ticket)
        self._repository.save(ticket)
        return ticket

    def attach_observer(self, ticket_id, observer):
        ticket = self._require_ticket(ticket_id)
        ticket.attach(observer)
        return ticket

    def resolve_ticket(self, ticket_id):
        ticket = self._require_ticket(ticket_id)
        ticket.resolve_ticket()
        return ticket

    def list_tickets(self):
        return self._repository.list_all()

    def _require_ticket(self, ticket_id):
        ticket = self._repository.get(ticket_id)
        if ticket is None:
            raise ValueError(f"Ticket with id {ticket_id} not found")
        return ticket
