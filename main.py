from appointment import Appointmentbook, MedicalAppointment, Businessmeeting

if __name__ == '__main__':
    book = Appointmentbook()
    appt1 = MedicalAppointment('detist visit', '2025-02-10','10:00 AM','Dr. smith', 'dental clinic')
    appt2 = Businessmeeting('Project update', '2025-02-11', '2:00 PM',['Mandela','Bob'],
                            'Conference room')
    book.add_appointment(appt1)
    book.add_appointment(appt2)

    print('appointments')
    book.show_appointments()

    appt1.reschedule('2025-02-12', '11:00 AM')

    print('updated appointments')
    book.show_appointments()