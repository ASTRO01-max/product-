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

    def to_dict(self):
        return {
            "pn": self.pn,
            "price": self.price,
            "amount": self.amount,
            "company": {
                "cn": self.company.cn,
                "year": self.company.year,
                "founder": self.company.founder
            }
        }

class Basket:
    def __init__(self):
        self.products = {} 

    def add(self, product):
        if product.pn in self.products:
            self.products[product.pn]["amount"] += product.amount 
        else:
            self.products[product.pn] = {
                "price": product.price,
                "amount": product.amount,
                "company": product.company
            }

    def remove(self, product_name, count):
        if product_name in self.products:
            if self.products[product_name]["amount"] > count:
                self.products[product_name]["amount"] -= count
                print(f"{count} ta {product_name} savatdan o'chirildi.")
            elif self.products[product_name]["amount"] == count:
                del self.products[product_name]
                print(f"{product_name} to'liq o'chirildi.")
            else:
                print(f"{product_name} savatda yetarli miqdorda emas.")
        else:
            print(f"{product_name} savatda topilmadi.")

    def view(self):
        if not self.products:
            print("Savat bo'sh.")
        else:
            for pn, details in self.products.items():
                print(f"Mahsulot: {pn}, Narxi: {details['price']}, Miqdori: {details['amount']}, Kompaniya: {details['company'].cn}")

    def total(self):
        summa = 0
        for details in self.products.values():
            summa += details["price"] * details["amount"]
        return summa

    def to_dict(self):
        return {
            "products": [
                {
                    "pn": pn,
                    "price": details["price"],
                    "amount": details["amount"],
                    "company": {
                        "cn": details["company"].cn,
                        "year": details["company"].year,
                        "founder": details["company"].founder
                    }
                } for pn, details in self.products.items()
            ],
            "total_price": self.total(),
        }

# Sinov uchun
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
b.remove("iPhone 15 Pro", 3)
print("\n3 ta iPhone 15 Pro o'chirildi:")
b.remove("iPhone 14", 5)
print("\niPhone 14 qisman o'chirildi:")

basket_dict = b.to_dict()
print("\nBasket as dictionary:")
print(basket_dict)

b.view()
