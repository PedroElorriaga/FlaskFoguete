from modulos.notificatorInterface import NotificatorInterface
from modulos.notificatorEmail import NotificatorEmail
from modulos.notificatorSMS import NotificatorSMS


# EXEMPLO DE CÓDIGO USANDO PRINCIPIOS DE DEPENDENCY INVERSION
class ClientNotification:
    def __init__(self, notificator_type: NotificatorInterface) -> None:
        self._notificator_type = notificator_type

    def send(self, message: str) -> None:
        self._notificator_type.send_notification(message)


client_email = NotificatorEmail()
clientEmail_instance = ClientNotification(client_email)
clientEmail_instance.send('Ola amigos')

client_SMS = NotificatorSMS()
clientSMS_instance = ClientNotification(client_SMS)
clientSMS_instance.send('Ola amigos')
