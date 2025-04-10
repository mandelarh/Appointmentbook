from abc import ABC, abstractmethod
class Appointment(ABC):
    #@abstractmethod
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time

    @abstractmethod
    def get_details(self):
        pass

    def reschedule(self, new_date, new_time):
        self.date = new_date
        self.time = new_time
        print(f"Appointment rescheduled to {self.date} at {self.time}")

class MedicalAppointment(Appointment):
    def __init__(self, title, date, time, doctor, location):
        super().__init__(title, date, time)
        self.doctor = doctor
        self.location = location

    def get_details(self):
        return f"Medical Appointment with {self.doctor} on {self.date} at {self.time}, Location: {self.location}"

class Businessmeeting(Appointment):
    def __init__(self, title, date, time, participants, location):
        super().__init__(title, date, time)
        self.participants = participants
        self.location = location
    def get_details(self):
        return f"Business meeting on {self.date} at {self.time}, with {','.join(self.participants)} at {self.location}"
class Appointmentbook:
    def __init__(self):
        self.appointments = []
    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def show_appointments(self):
        for appt in self.appointments:
            print(appt.get_details())

    def remove_appointment(self, title):
        self.appointments = [appt for appt in self.appointments if appt.title != title]