import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv")
pdf = FPDF(orientation="P", unit="mm", format='A4')


class Product:
    def __init__(self, ID):
        self.ID = ID

    def product_details(self):
        product_name = df.loc[df['id'].astype(str) == self.ID, 'name'].squeeze()
        product_price = str(df.loc[df['id'].astype(str) == self.ID, 'price'].squeeze())
        return product_name, product_price

    def available(self):
        number = df.loc[df['id'].astype(str) == self.ID, 'in stock'].squeeze()
        return number



class Receipt:
    def __init__(self, ID, product_name, product_price):
        self.ID = ID
        self.product_name = product_name
        self.product_price = product_price


    def generate_receipt(self):
        pdf.add_page()
        pdf.set_font(family='Arial', style='', size=12)
        pdf.cell(w=40, h=10, txt=f"Product ID: {self.ID}", ln=1, align='L')
        pdf.cell(w=40, h=10, txt=f"Product Name: {self.product_name}", ln=1, align='L')
        pdf.cell(w=40, h=10, txt=f"Product Price: {self.product_price}", ln=1, align='L')
        pdf.output("receipt.pdf")


print(df)
id = input("Enter the product ID ")
product = Product(id)
product_name, product_price = product.product_details()

if product.available():
    receipt = Receipt(id, product_name, product_price)
    receipt_pdf= receipt.generate_receipt()


