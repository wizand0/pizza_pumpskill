"# pizza_pumpskill" 
# pizza_pumpskill

## Задача: написать программу для создания пиццы из ингредиентов с возможностью расчета общей калорийности и себестоимости конечного продукта.

### Описание логики: есть продукт - тесто, помидорка или сыр. У продукта есть характеристики: название, калорийность и себестоимость. Например, тесто имеет калорийность 200 Ккал на 100 грамм, а стоит оно 20 рублей за 100 грамм.

### Из продуктов состоит ингредиент пиццы. Ингредиент - это сам продукт и вес продукта. Примеры ингредиентов:

Ингредиент #1: 300 грамм теста;
Ингредиент #2: 50 грамм помидор;
Ингредиент #3: 100 грамм сыра.
Из ингредиентов состоит пицца. Например, состав пиццы “Маргарита” будет следующий:

Ингредиент #1;
Ингредиент #2;
Ингредиент #3.
Состав пиццы “Маргарита лайт (без томатов)” следующий:

Ингредиент #1;
Ингредиент #3.
Требования:

### Необходимо создать следующие классы:

### 1. Класс Product

Атрибуты:

title: название. Обязательный атрибут. Не может быть пустым;
calorific: калорийность на 100 грамм. Обязательный. Только положительное число;
cost: себестоимость: цена за 100 грамм продукта. Обязательный. только положительное число.
### 2. Класс Ingredient

Атрибуты:

product: класс Product;
weight: вес. Обязательный атрибут. Только положительное число.
Методы:

get_calorific: возвращает калорийность ингредиента по формуле: вес_ингредиента / 100 * калорийность_продукта;
get_cost: возвращает себестоимости ингредиента по формуле: вес_ингредиента / 100 * себестоимость_продукта;
### 3. Класс Pizza

Атрибуты:

title - название. Обязательный атрибут. Не может быть пустым;
ingredients - ингредиенты. Список значений класса Ingredient.
Методы:

get_calorific: возвращает общую калорийность пиццы как сумма калорийности всех ингредиентов, из которых состоит пицца;
get_cost: возвращает общую себестоимости пиццы как сумма себестоимости всех ингредиентов, из которых состоит пицца.
Программа должна предоставлять следующие возможности:

Создать продукт с указанием названия, калорийности и себестоимости;
Создать ингредиент из продукта с указанием веса;
Создать пиццу с указанием названия и списка из ингредиентов;
При выводе пиццы функцией print() должно выводиться ее название, общая калорийность и общая себестоимость.
Что будет проверяться
*Класс Product создан корректно
*Класс Ingredient создан корректно
*Класс Pizza создан корректно
*Автотест пройден без ошибок
