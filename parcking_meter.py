
class Car:
    def __init__(self, brand, model, color, license_num):
        self.brand = brand
        self.model = model
        self.color = color
        self.license_num = license_num

    def __str__(self):
        return 'Time to issue a ticket\nBrand:{:s}\nModel:{:s}\nColor:{:s}\nLicence Number:{:s}'\
            .format(self.brand, self.model, self.color, self.license_num)


class OfficerData:
    def __init__(self, name, badge_num):
        self.name = name
        self.badge_num = badge_num

    def issue_ticket(self, parking_meter, car):
        print(car)
        print(self)
        parking_meter.fine()
        print('Minutes illegaly parked:{:d}\nFine:{:d}'.format(parking_meter.illegal_parking_time(),
                                                                   parking_meter.fine()))
    @staticmethod
    def time_check(parking_meter):
        park_check = False

        if parking_meter.paid >= parking_meter.time:
            park_check = True

        return park_check

    def __str__(self):
        return 'Officer Data:\nName:{:s}\nBadge Number:{:s}'.format(self.name, self.badge_num)


class ParkingMeter:

    def __init__(self, paid, time):
        self.paid = paid
        self.time = time

    def fine(self):
        total_fine = 20
        additional_hour_fine = 10
        additional_time = self.time - self.paid
        additional_time_in_hour = round(additional_time / 60)
        total_fine = total_fine + (additional_hour_fine * additional_time_in_hour)

        return total_fine

    def illegal_parking_time(self):
        illegal_time = self.time - self.paid

        return illegal_time

    def __str__(self):
        return 'Number of minutes for in the meter:{:d}\nNumber of minutes car has been parked:{:d}\n'\
            .format(self.paid, self.time)


officer_1 = OfficerData('joe', '1234567')

paid = int(input('Number of minutes for in the meter:'))
time = int(input('Number of minutes car has been parked:'))
parking_meter = ParkingMeter(paid, time)

if officer_1.time_check(parking_meter):
    print('Nothing to see here')

else:
    brand = input('Brand:')
    model = input('Model:')
    color = input('Color:')
    license_num = input('Licence Number:')
    car_1 = Car(brand, model, color, license_num)
    officer_1.issue_ticket(parking_meter, car_1)
