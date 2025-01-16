from datetime import datetime
class FoodProduct:
    def __init__(self, name:str, price:float, category:str, production_date:datetime, expiration_date:datetime):
        self.__name = name
        self.__price = price
        self.__category = category
        self.__production_date = production_date
        self.__expiration_date = expiration_date

    def __add__(self, other):
        if isinstance(other, int):
            return self.__price + other
        else:
            raise TypeError(f"Price must be of type int or {type(other)}")



    def __sub__(self, other):
        if isinstance(other, int):
            return self.__price - other
        raise TypeError(f"Price must be of type int or {type(other)}")

    def __mul__(self, other):
       if isinstance(other, int):
            return self.__price * other
       raise TypeError(f"Price must be of type int or {type(other)}")

    def __eq__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price == other.__price
        elif isinstance(other, int):
            return self.__price == other
        raise TypeError(f"Price must be of type int or {type(other)}")

    def __ne__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price != other.__price
        elif isinstance(other, int):
            return self.__price != other
        raise TypeError(f"Price must be of type int or {type(other)}")

    def __gt__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price > other.__price
        elif isinstance(other, int):
            return self.__price > other
        raise TypeError(f"Price must be of type int or {type(other)}")

    def __lt__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price < other.__price
        elif isinstance(other, int):
            return self.__price < other
        raise TypeError(f"Price must be of type int or {type(other)}")

    def __hash__(self):
        return hash(self.__price)

    def __len__(self):
        return (datetime.now()-self.__production_date).days


    def __str__(self):
        return f"Product Name: {self.__name}\nPrice: {self.__price}\nCategory: {self.__category}\
        \nProduction Date: {self.__production_date}\nExpiration Date: {self.__expiration_date}"

    def __repr__(self):
        return f"FoodProduct({self.__name}, {self.__price}, {self.__category}, {self.__production_date}, {self.__expiration_date})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if not new_name.isdigit and len(new_name)>3 and new_name:
                self.__name = new_name
            else:
                raise ValueError(f"Name must be only characters, and therefore can't be {new_name}")
        else:
            raise TypeError(f"Name must be str, and can't be {type(new_name)}")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, int) or isinstance(new_price, float):
            if 0.1 <= new_price <= 100:
                self.__price = new_price
            else:
                raise ValueError(f"Price must be between 0.1 and 100. It certainly can't be {new_price}")
        else:
            raise TypeError(f"Price must be int or float must be str, and can't be {type(new_price)}")

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if not new_category.isdigit:
                if new_category in ['Meat'.lower(), 'Dairy'.lower(), 'Parve'.lower()]:
                    self.__category = new_category
                else:
                    raise ValueError(f"Category must be only 'Meat', 'Dairy' or 'Parve'. It can't be {new_category}")
            else:
                raise ValueError(f"Category must be only characters, and therefore can't be {new_category}")
        else:
            raise TypeError(f"Category must be str, and can't be {type(new_category)}")

    @property
    def production_date(self):
        return self.__production_date

    @production_date.setter
    def production_date(self, new_production_date):
        if isinstance(new_production_date, datetime):
            if new_production_date <= datetime.now():
                self.__production_date = new_production_date
            else:
                raise ValueError(f"Production Date can't be later then the current date")
        else:
            raise TypeError(f"Date must be of type datetime, and cant be {type(new_production_date)}")

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, new_expiration_date):
        if isinstance(new_expiration_date, datetime):
            if (new_expiration_date - datetime.now()) >= 7:
                self.__expiration_date = new_expiration_date
            else:
                raise ValueError(f"Expiration date must be at least 1 week ahead of the current date!")
        else:
            raise TypeError(f"Date must be of type datetime, and cant be {type(new_expiration_date)}")

    @property
    def remaining(self):
        remaining_days = (self.__expiration_date - datetime.now()).days
        if remaining_days >= 0:
            return remaining_days
        else:
            raise ValueError(f"Date has already expired!")




first = FoodProduct('Milk', 5, 'Dairy', datetime.strptime('16/1/2024', '%d/%m/%Y'), datetime.strptime('27/3/2026', '%d/%m/%Y'))
second = FoodProduct('Cottage', 7, 'Dairy', datetime.strptime('15/3/2024', '%d/%m/%Y'), datetime.strptime('20/4/2024', '%d/%m/%Y'))
third = FoodProduct('Chicken Breast', 39.9, 'Meat', datetime.strptime('9/9/2024', '%d/%m/%Y'), datetime.strptime('1/2/2025', '%d/%m/%Y'))

print(first)
print(second)
print(first.price+second.price)
print(first+1)
# print(first+"banana")

print(first.price-second.price)
print(first==second)
print(first>second)
print(first<second)
print(first.price*second.price)
print(first!=second)
print(hash(first))
print(len(first))
print(first)
print(first.remaining)
