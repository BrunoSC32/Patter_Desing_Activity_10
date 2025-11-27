import abc
from datetime import datetime


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, message):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        print(f"--- [SYSTEM] Sending notification... ---")
        for observer in self._observers:
            observer.update(message)


class Ticket(Subject, abc.ABC):
    def __init__(self, ticket_id, description):
        super().__init__()
        self.ticket_id = ticket_id
        self.description = description
        self.status = "OPEN"

    @abc.abstractmethod
    def display_info(self):
        pass

    def resolve_ticket(self):
        self.status = "RESOLVED"
        date_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.notify_observers(
            f"Your ticket #{self.ticket_id} has been resolved at {date_str}"
        )


class TicketRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, ticket):
        pass

    @abc.abstractmethod
    def get(self, ticket_id):
        pass

    @abc.abstractmethod
    def list_all(self):
        pass
