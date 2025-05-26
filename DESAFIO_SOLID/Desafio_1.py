'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''
from abc import ABC, abstractmethod


class TaskHandler(ABC):
    @abstractmethod
    def conect_api():
        pass

    @abstractmethod
    def send_notification():
        pass

    @abstractmethod
    def generate_report():
        pass

    @abstractmethod
    def send_report():
        pass


class CreateNewTask(TaskHandler):
    def conect_api(self):
        print('Connection to API was successful!')

    def send_notification(self, message: str):
        print(message)

    def generate_report(self):
        print('Report generated')

    def send_report(self):
        print('Report sent')

    def create_task(self):
        self.conect_api()
        self.generate_report()
        self.send_report()
        self.send_notification('New task created')


class UpdateTask(TaskHandler):
    def conect_api(self):
        print('Connection to API was successful!')

    def send_notification(self, message: str):
        print(message)

    def generate_report(self):
        print('Report generated')

    def send_report(self):
        print('Report sent')

    def update_task(self):
        self.conect_api()
        self.generate_report()
        self.send_report()
        self.send_notification('Task updated')


class RemoveTask(TaskHandler):
    def conect_api(self):
        print('Connection to API was successful!')

    def send_notification(self, message: str):
        print(message)

    def generate_report(self):
        print('Report generated')

    def send_report(self):
        print('Report sent')

    def remove_task(self):
        self.conect_api()
        self.generate_report()
        self.send_report()
        self.send_notification('Task removed')
