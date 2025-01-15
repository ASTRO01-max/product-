class Company:
    def __init__(self, cn, year, founder):
        self.cn = cn
        self.year = year
        self.founder = founder

class Product:
    def __init__(self, pn, price, amount, company):
        self.pn = pn 
        self.price = price
        self.amount = amount
        self.company = company

    def __str__(self):
        return f"Mahsulot: {self.pn}, Narxi: {self.price}, Miqdori: {self.amount}, Kompaniya: {self.company.cn}"

class Basket:
    def __init__(self):
        self.products = []

    def add(self, product):
        for i in self.products:
            if i.pn == product.pn:  
                i.amount += product.amount 
                return
        self.products.append(product)  

    def remove(self, product_name):
        self.products = [p for p in self.products if p.pn != product_name]  

    def view(self):
        for i in self.products:
            print(i)

    def total(self):
        summa = 0
        for product in self.products:
            summa += product.price * product.amount
        return summa

c1 = Company("Apple", 1990, "Steve Jobs")
pr1 = Product("iPhone 15 Pro", 800, 10, c1)
pr2 = Product("iPhone 15 Pro", 800, 5, c1)
pr3 = Product("iPhone 14", 700, 3, c1)

b = Basket()
b.add(pr1)
b.add(pr2)
b.add(pr3)

print("Products:")
b.view()
print(f"Total: {b.total()} USD")

b.remove("iPhone 14")
print("Products removed from cart:")
b.view()