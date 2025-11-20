from factories import TicketFactory
from decorators import UrgentDecorator
from implements import ITUser


def main():
    print("=== IT TICKET SYSTEM (Modular & Patterns) ===\n")

    user_john = ITUser("John Doe (Employee)")
    admin_support = ITUser("IT Support Center")

    try:
        ticket1 = TicketFactory.create_ticket("network", 101, "Wifi Connection Failed on 2nd Floor")

        ticket1.attach(user_john)

        ticket1.attach(admin_support)

        print(f"Created: {ticket1.display_info()}")


        urgent_ticket = UrgentDecorator(ticket1)

        print(f"Current State: {urgent_ticket.display_info()}")


        print("\n3. Resolving ticket...")
        urgent_ticket.resolve_ticket()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()