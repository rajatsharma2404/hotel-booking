import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id':str})

class Hotel:
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


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object


    def generate(self):
        content = f"""Thank you for the reservation.
Your booking details are:
Name : {self.customer_name}
Hotel : {self.hotel.hotel_name}."""
        return content



print(df)
hotel_ID = input("enter id of hotel ")

hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name ")
    generate_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(generate_ticket.generate())

else:
    print("Hotel doesn't exist!")