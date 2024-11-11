class Product:
    def __init__(self,id,
                 product,
                 category,
                 sub_category,
                 brand,
                 sale_price,
                 market_price,
                 type,
                 rating,
                 description):
        self.__id=id
        self.__product=product
        self.__category=category
        self.__sub_category=sub_category
        self.__brand=brand
        self.__sale_price=sale_price
        self.__market_price=market_price
        self.__type=type
        self.__rating=rating
        self.__description=description

    def imprimir(self):
        print('ID: ',self.__id)
        print('Product: ',self.__product)
        print('Category: ',self.__category)
        print('Sub-Category: ',self.__sub_category)
        print('Brand: ',self.__brand)
        print('Sale-Price: ', self.__sale_price)
        print('Market-Price: ', self.__market_price)
        print('Type: ', self.__type)
        print('Rating: ',self.__rating)
        print('Description: ', self.__description)

        return "----------------"
    
    def getName(self):
        return self.__product
    def getCategory(self):
        return self.__category
    def getsubCategory(self):
        return self.__sub_category
    def getBrand(self):
        return self.__brand
    def getSalePrice(self):
        return self.__sale_price
    def getMarketPrice(self):
        return self.__market_price
    def getType(self):
        return self.__type
    def getRating(self):
        return self.__rating
    def getDescription(self):
        return self.__description