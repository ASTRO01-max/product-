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

    def remove(self, product_name, count):
        for product in self.products:
            if product.pn == product_name:
                if product.amount > count:
                    product.amount -= count
                    print(f"{count} ta {product_name} savatdan o'chirildi.")
                elif product.amount == count:
                    self.products.remove(product)
                    print(f"{product_name} to'liq o'chirildi.")
                return
        print(f"{product_name} savatda topilmadi.")

    def view(self):
        if not self.products:
            print("Savat bo'sh.")
        else:
            for i in self.products:
                print(i)

    def total(self):
        summa = 0
        for product in self.products:
            summa += product.price * product.amount
        return summa
    
    def to_dict(self):
        return {
            "products": [product.to_dict() for product in self.products],
            "total_price": self.total(),
        }


c1 = Company("Apple", 1990, "Steve Jobs")
pr1 = Product("iPhone 15 Pro", 800, 10, c1)
pr2 = Product("iPhone 15 Pro", 800, 5, c1)
pr3 = Product("iPhone 14", 700, 10, c1)
pr4 = Product("Samsung S24 Ultra", 1200, 14, c1)

b = Basket()
b.add(pr1)
b.add(pr2)
b.add(pr3)
b.add(pr4)

print("Products:")
print(f"Total: {b.total()} USD")
b.view()

b.remove("iPhone 15 Pro", 3)
print("\n3 ta iPhone 15 Pro o'chirildi:")

b.remove("iPhone 14", 5)
print("\niPhone 14 o'chirildi:")
b.view()

basket_dict = Basket.to_dict()
print(basket_dict)
