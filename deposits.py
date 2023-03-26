print("Hi! This tool will help you calculate profits for your deposit")

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

print("The current deposit rates is as follows ")
print(list(per_cent.keys())[0] + " " + str(list(per_cent.values())[0]))
print(list(per_cent.keys())[1] + " " + str(list(per_cent.values())[1]))
print(list(per_cent.keys())[2] + " " + str(list(per_cent.values())[2]))
print(list(per_cent.keys())[3] + " " + str(list(per_cent.values())[3]))

money = input("Please enter the value of your deposit: ")

deposit = [int(money)*(per_cent['ТКБ']/100), int(money)*(per_cent['СКБ']/100), int(money)*(per_cent['ВТБ']/100), int(money)*(per_cent['СБЕР']/100)]
print("Here is what you can earn " + str(deposit))
print("The maximum yearly profit is " + str(max(deposit)))

