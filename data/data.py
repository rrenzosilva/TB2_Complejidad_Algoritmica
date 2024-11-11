import csv
import sys

sys.path.append('./data/entity')

from calculo import calculo
from product import Product
from grafo import Grafo


def ReadData(category, sub_category, sale_price, market_price, rating):
    grafoPadre = Grafo("Padre")

    category = {
        "": 0,
        "Baby Care": 1,
        "Bakery, Cakes & Dairy": 2,
        "Beauty & Hygiene": 3,
        "Beverages": 4,
        "Cleaning & Household": 5,
        "Eggs, Meat & Fish": 6,
        "Foodgrains, Oil & Masala": 7,
        "Fruits & Vegetables": 8,
        "Gourmet & World Food": 9,
        "Kitchen, Garden & Pets": 10,
        "Snacks & Branded Foods": 11
    }

    sub_category = {
        "All Purpose Cleaners": 1,
        "Appliances & Electricals": 2,
        "Atta, Flours & Sooji": 3,
        "Baby Accessories": 4,
        "Baby Bath & Hygiene": 5,
        "Baby Food & Formula": 6,
        "Bakery Snacks": 7,
        "Bakeware": 8,
        "Bath & Hand Wash": 9,
        "Bins & Bathroom Ware": 10,
        "Biscuits & Cookies": 11,
        "Breads & Buns": 12,
        "Breakfast Cereals": 13,
        "Cakes & Pastries": 14,
        "Car & Shoe Care": 15,
        "Cereals & Breakfast": 16,
        "Chocolates & Biscuits": 17,
        "Chocolates & Candies": 18,
        "Coffee": 19,
        "Cookies, Rusk & Khari": 20,
        "Cooking & Baking Needs": 21,
        "Cookware & Non Stick": 22,
        "Crockery & Cutlery": 23,
        "Cuts & Sprouts": 24,
        "Dairy": 25,
        "Dairy & Cheese": 26,
        "Dals & Pulses": 27,
        "Detergents & Dishwash": 28,
        "Diapers & Wipes": 29,
        "Disposables, Garbage Bag": 30,
        "Drinks & Beverages": 31,
        "Dry Fruits": 32,
        "Edible Oils & Ghee": 33,
        "Eggs": 34,
        "Energy & Soft Drinks": 35,
        "Exotic Fruits & Veggies": 36,
        "Feeding & Nursing": 37,
        "Feminine Hygiene": 38,
        "Fish & Seafood": 39,
        "Flask & Casserole": 40,
        "Fragrances & Deos": 41,
        "Fresh Fruits": 42,
        "Fresh Vegetables": 43,
        "Fresheners & Repellents": 44,
        "Frozen Veggies & Snacks": 45,
        "Fruit Juices & Drinks": 46,
        "Gardening": 47,
        "Gourmet Breads": 48,
        "Hair Care": 49,
        "Health & Medicine": 50,
        "Health Drink, Supplement": 51,
        "Herbs & Seasonings": 52,
        "Ice Creams & Desserts": 53,
        "Indian Mithai": 54,
        "Kitchen Accessories": 55,
        "Makeup": 56,
        "Masalas & Spices": 57,
        "Men's Grooming": 58,
        "Mops, Brushes & Scrubs": 59,
        "Mutton & Lamb": 60,
        "Non Dairy": 61,
        "Noodle, Pasta, Vermicelli": 62,
        "Oils & Vinegar": 63,
        "Oral Care": 64,
        "Oraln Care": 65,
        "Organic Fruits & Vegetables": 66,
        "Organic Staples": 67,
        "Party & Festive Needs": 68,
        "Pasta, Soup & Noodles": 69,
        "Pet Food & Accessories": 70,
        "Pickles & Chutney": 71,
        "Pooja Needs": 72,
        "Ready To Cook & Eat": 73,
        "Rice & Rice Products": 74,
        "Salt, Sugar & Jaggery": 75,
        "Sauces, Spreads & Dips": 76,
        "Sausages, Bacon & Salami": 77,
        "Skin Care": 78,
        "Snacks & Namkeen": 79,
        "Snacks, Dry Fruits Nuts": 80,
        "Spreads, Sauces, Ketchup": 81,
        "Stationery": 82,
        "Steel Utensils": 83,
        "Storage & Accessories": 84,
        "Tea": 85,
        "Tinned & Processed Food": 86,
        "Water": 87
    }

    with open('./data/datos.csv') as data:
        next(data)
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            product = Product(row[0], row[1], row[2], row[3], row[4], row[5], int(row[6]), int(row[7]), row[8],
                              int(row[9]), row[10])
            grafoPadre.Agregar_Vertice(product)
        return grafoPadre

