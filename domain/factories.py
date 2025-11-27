from .implements import NetworkTicket, SoftwareTicket

class TicketFactory:

    @staticmethod
    def create_ticket(ticket_type, ticket_id, description):
        t_type = ticket_type.lower()

        if t_type == "network":
            return NetworkTicket(ticket_id, description)
        elif t_type == "software":
            return SoftwareTicket(ticket_id, description)
        else:
            raise ValueError("Invalid ticket type")
