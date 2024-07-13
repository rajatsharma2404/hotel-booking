import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id':str})
card_df= pd.read_csv("card_security.csv", dtype=str).to_dict(orient='records')
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


class CreditCard:

    def __init__(self, number):
        self.number = number

    def validate(self,password):
        card_details = {'number':self.number, 'password': password}
        if card_details in card_df:
            return True
        else:
            return False



print(df)
hotel_ID = input("enter id of hotel ")

hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(number = "1234567890123456")

    if credit_card.validate(password='mypass'):
        hotel.book()
        name = input("Enter your name ")
        generate_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
        print(generate_ticket.generate())

    else:
        print("Something wrong with the payment!")

else:
    print("Hotel is full!")