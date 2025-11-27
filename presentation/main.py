from domain.implements import ITUser
from domain.ticket_service import TicketService
from infrastructure.in_memory_ticket_repository import InMemoryTicketRepository


def main():
    print("=== IT TICKET SYSTEM (Modular & Patterns) ===\n")
    repository = InMemoryTicketRepository()
    service = TicketService(repository)

    user_john = ITUser("John Doe (Employee)")
    admin_support = ITUser("IT Support Center")

    try:
        urgent_ticket = service.create_ticket(
            "network",
            101,
            "Wifi Connection Failed on 2nd Floor",
            urgent=True,
        )

        service.attach_observer(urgent_ticket.ticket_id, user_john)
        service.attach_observer(urgent_ticket.ticket_id, admin_support)

        print(f"Created: {urgent_ticket.display_info()}")

        print("\nCurrent tickets in repository:")
        for ticket in service.list_tickets():
            print(f" - {ticket.display_info()} [{ticket.status}]")

        print("\nResolving ticket through service...")
        service.resolve_ticket(urgent_ticket.ticket_id)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
