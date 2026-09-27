print("=====CREATING 2 SETS=====")
basket1 = {"apple", "cucumber", "grapes", "pineapple", "mango"}
basket2 = {"Kiwi", "Kiwi", "mango," "cucumber", "grape", "pineapple", "papaya"}

print("Basket 1= ", basket1)
print("Basket 2= ", basket2)


print("\n =====ADDING A NEW FRUIT TO A BASKET=====")
basket1.add("Mandarin")
print("New basket1: ", basket1)

print("\n=====COMMON FRUITS IN BOTH BASKETS=====")

common_fruits = basket1.intersection(basket2)
print("Common fruits in  both baskets: ", common_fruits)

print("\n=====CREATING AN ARRAY=====")
import array as arr
fruitss_count = arr.array('i', [4, 5, 8, 3, 3, 2])
print("Fruit coint array: ", fruitss_count)