import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id':str})
card_df= pd.read_csv("cards.csv", dtype=str).to_dict(orient='records')
security_details_df = pd.read_csv("card_security.csv", dtype=str)
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

class SpaHotel(Hotel):

    def book(self):
        pass


class SpaReservation:

    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""Thank you for the reservation.
        Your booking details are:
        Name : {self.customer_name}
        Hotel : {self.hotel.hotel_name}."""
        return content




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

    def validate(self,expiration, cvc, holder):
        card_details = {'number':self.number, 'expiration':expiration, 'cvc' :cvc, 'holder' :holder}
        if card_details in card_df:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = security_details_df.loc[security_details_df['number'] == self.number, 'password'].squeeze()
        if given_password == password:
            return True
        else:
            return False






print(df)
hotel_ID = input("enter id of hotel ")

hotel = SpaHotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number = "1234")

    if credit_card.validate(expiration='12/26', cvc = '123', holder = 'JOHN SMITH'):
        passw = input("Enter you card password ")
        if credit_card.authenticate(passw):
            hotel.book()
            name = input("Enter your name ")
            generate_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(generate_ticket.generate())

            #Code for spa booking
            spa_bool = input("Do you need a spa booking?")
            if spa_bool == 'Yes':
                spa_hotel = SpaHotel(hotel_ID)
                generate_spa_ticket = SpaReservation(customer_name = name, hotel_object = hotel)
                print(generate_spa_ticket.generate())

        else:
            print("Wrong password!")

    else:
        print("Something wrong with the payment!")

else:
    print("Hotel is full!")