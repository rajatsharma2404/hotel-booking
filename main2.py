import pandas as pd

from abc import ABC, abstractmethod #Use to create abstract class

df = pd.read_csv("hotels.csv", dtype={'id':str})


class Hotel:

    watermark = "The Udaipur Hotel"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id'] == hotel_id, 'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df['id'] == self.hotel_id]['available'].squeeze()

        if availability == "yes":
            return True
        else:
            return False

    #important to add the decorator
    @classmethod
    def get_count_hotel(cls, data):
        return len(data)

    #Magic Method
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True

class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generatee(self):
        content = f"""Thank you for the reservation.
Your booking details are:
Name : {self.customer_name}
Hotel : {self.hotel.hotel_name}."""
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        return name



hotel1 = Hotel("188")

print(Hotel.get_count_hotel(df))
print(hotel1.get_count_hotel(df))

reservation = ReservationTicket(customer_name="Raj Sharma ", hotel_object=hotel1)
print(reservation.customer_name) #property is a method which behaves like a variable
