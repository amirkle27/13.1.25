from datetime import datetime
import sqlite3

connection = sqlite3.connect("product.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


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



milk = FoodProduct('Milk', 5, 'Dairy', datetime.strptime('16/1/2024', '%d/%m/%Y'), datetime.strptime('27/3/2026', '%d/%m/%Y'))
cottage = FoodProduct('Cottage', 7, 'Dairy', datetime.strptime('15/3/2024', '%d/%m/%Y'), datetime.strptime('20/4/2024', '%d/%m/%Y'))
chicken_breast = FoodProduct('Chicken Breast', 39.9, 'Meat', datetime.strptime('9/9/2024', '%d/%m/%Y'), datetime.strptime('1/2/2025', '%d/%m/%Y'))
waffles = FoodProduct('Waffles', 14.5, 'Parve', datetime.strptime('13/1/2025', '%d/%m/%Y'), datetime.strptime('15/3/2025', '%d/%m/%Y'))

products_just_for_tryout = [milk,cottage, chicken_breast, waffles]


print(milk)
print(cottage)
print(milk.price+cottage.price)
print(milk+1)
print(milk.price-cottage.price)
print(milk==cottage)
print(milk>cottage)
print(milk<cottage)
print(milk.price*cottage.price)
print(milk!=cottage)
print(hash(milk))
print(len(milk))
print(milk)
print(milk.remaining)
print(waffles)

cursor.execute("""
CREATE TABLE IF NOT EXISTS FoodProducts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price TEXT NOT NULL,
    category TEXT NOT NULL,
    production_date TEXT NOT NULL,
    expiration_date TEXT NOT NULL)
    """)
connection.commit()


def get_and_insert_product(curser):
    while True:
        new_product = input("Do you wish to add a new product?\n"
                            "If yes, please enter: Product Name, price, category, production_date (dd/mm/yyyy), expiration_date (dd/mm/yyyy)\n"
                            "Otherwise, type 'no' or 'n' to quit\n").strip()

        if new_product.lower() in ("n", "no"):
            print(f"Thank you\nGoodbye.")
            break

        else:
            try:
                product_data = new_product.split(",")
                if len(product_data) != 5:
                    print("Invalid input. Product must have 5 details: Product Name, price, category, production_date (dd/mm/yyyy), expiration_date (dd/mm/yyyy)\n"
                          "Please try again")
                    continue
                name = str(product_data[0].strip())
                price = float(product_data[1].strip())
                category = str(product_data[2].strip())
                production_date = datetime.strptime(product_data[3].strip(), '%d/%m/%Y')
                expiration_date = datetime.strptime(product_data[4].strip(), '%d/%m/%Y')

                product = FoodProduct(name, price, category, production_date, expiration_date)

                existing_product = curser.execute("""
                SELECT * FROM FoodProducts WHERE name = ?""", (name,)).fetchone()
                if existing_product:
                    print(f"Product {name} already exits in the database.")
                else:
                    insert_product(curser, product)
            except Exception as e:
                print(f"An error occurred with: {e}. Please try again")
            show_table = input("Would you like to see the full products list?")
            if show_table.lower() in ("n", "no"):
                print("Thank you, goodbye")
                break
            else:
                show_products(cursor)
                
def insert_product(curser, product):
    query = """
                        INSERT INTO FoodProducts (name, price, category, production_date, expiration_date) VALUES
                        (?,?,?,?,?)"""
    curser.execute(query,
                   (product.name, product.price, product.category, product.production_date, product.expiration_date))
    curser.connection.commit()
    product_id = curser.execute("""SELECT id FROM FoodProducts WHERE name = ?""", (product.name,)).fetchone()
    print(f"Product{product.name} added to db with id: {product_id[0]}")


def insert_a_list_of_products(cursor,list):
    for product in list:
        insert_product(cursor, product)
        print(f"{product}\n")


def show_products(cursor):
    products = cursor.execute("""SELECT * FROM FoodProducts""").fetchall()
    for row in products:
        product = FoodProduct(
            name=row['name'],
            price=row['price'],
            category = row['category'],
            production_date = datetime.strptime(row['production_date'], '%Y-%m-%d %H:%M:%S'),
            expiration_date = datetime.strptime(row['expiration_date'], '%Y-%m-%d %H:%M:%S')
        )
        print(f"{product}\n")



get_and_insert_product(cursor)

show_products(cursor)

insert_a_list_of_products(cursor,products_just_for_tryout)


# def drop_table (cursor, table_to_drop):
#     cursor.execute(f"DROP TABLE {table_to_drop}")
#     print( f"table {table_to_drop} dropped")
#
# drop_table(cursor,'FoodProducts')
