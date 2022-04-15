class Product:
    def __init__(self, title, calorific, cost):
        if calorific <= 0 or title == '' or cost <= 0:
            raise ValueError('Значение атрибутов может быть только положительным')
        else:
            self.__title = title
            self.__calorific = calorific
            self.__cost = cost

    def __str__(self):
        return f'Название продукта: {self.title}; Калорийность: {self.calorific}; Цена: {self.cost}.'

    @property
    def calorific(self):
        return self.__calorific

    @calorific.setter
    def calorific(self, value):
        if value <= 0:
            raise ValueError('Значение атрибута calorific может быть только положительным')
        else:
            self.calorific = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Значение атрибута title не может быть пустым')
        else:
            self.title = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value <= 0:
            raise ValueError('Значение атрибута cost может быть только положительным')
        else:
            self.calorific = value


class Ingredient(Product):
    def __init__(self, product, weight):
        if weight <= 0:
            raise ValueError('Значение атрибутов может быть только положительным')
        else:
            super().__init__(product.title, product.calorific, product.cost)
            self.__weight = weight

    def __str__(self):
        str_temp = super().__str__()
        return f'Ингридиент состоит из: {str_temp}; При этом вес: {self.weight}.'

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('Значение атрибута weight не может быть пустым')
        else:
            self.weight = value

    def get_calorific(self):
        result = super().calorific
        return self.weight / 100 * result

    def get_cost(self):
        return self.weight / 100 * super().cost


class Pizza:
    def __init__(self, title, ingredients):
        if title == '':
            raise ValueError('Значение атрибутов может быть только положительным')
        else:
            self.__title = title
            self.__ingredients = ingredients

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Значение атрибута title не может быть пустым')
        else:
            self.title = value

    def get_calorific(self):
        calories = 0
        for el in self.__ingredients:
            calories += el.get_calorific()
        return calories

    def get_cost(self):
        cost = 0
        for el in self.__ingredients:
            cost += el.get_cost()
        return cost

    def __str__(self):

        tmp_calor = self.get_calorific()
        tmp_price = self.get_cost()
        return f'{self.__title} ({tmp_calor} kkal) - {tmp_price} руб'


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты.
# Для каждого ингредиента указываем продукт, из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
pizza_margarita_light = Pizza('Маргарита', [dough_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(pizza_margarita)
print(pizza_margarita_light)
