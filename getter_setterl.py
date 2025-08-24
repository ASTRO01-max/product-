class Pupil:
    def __init__(self, name, year, subject):
        self.name = str(name)
        self.year = int(year)
        self.subject = str(subject)

    def get_name(self):
        return "name: " + self.name

    def set_name(self, new_name):
        if new_name.isdigit():
            print("Ism faqat harflardan iborat bo'lishi kerak!")
            return
        self.name = new_name

    def get_year(self):
        return "yili: " + str(self.year)  
    
    def set_year(self, new_year):
        if not new_year.isdigit():
            print("Tug'ilgan yilda faqat raqamlar bo'lishi kerak!")
            return
        self.year = int(new_year)  

    def get_subject(self):
        return "fani: " + self.subject
    
    def set_subject(self, new_subject):
        if new_subject.isdigit():
            print("Fan nomi faqat harflardan iborat bo'lishi kerak!")
            return
        self.subject = new_subject  

p1 = Pupil("Yusuf", 2008, "Python")  
p1.set_name("12")  
print(p1.get_name()) 

p1.set_year("abcd")  
p1.set_year("2008")  
print(p1.get_year()) 

p1.set_subject("123")  
p1.set_subject("Python")  
print(p1.get_subject())  
