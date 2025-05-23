from .notificatorInterface import NotificatorInterface


class NotificatorEmail(NotificatorInterface):
    def send_notification(self, message: str) -> None:
        print(f'Sending notification from Email: {message}')
