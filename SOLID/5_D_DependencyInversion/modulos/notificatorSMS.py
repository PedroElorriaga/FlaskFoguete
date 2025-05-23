from .notificatorInterface import NotificatorInterface


class NotificatorSMS(NotificatorInterface):
    def send_notification(self, message: str) -> None:
        print(f'Sending notification from SMS: {message}')
