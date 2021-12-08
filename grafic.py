import matplotlib.pyplot as plt

Plan = [11707.20,11707.20,14236.60,1566.03]
Fact = [10922.80,16000.20,14000.70,1540.08]
percent = [93.30,100.60,98.34,98.34]
prod_plan = [260.16,345.77,316.37,316.37]
prod_fact = [273.07,355.56,325.60,325.60]
cvar = [1,2,3,4]
plt.plot(cvar,Plan,label = "Товарообіг план. 'Галактон'")
plt.plot(cvar,Fact,label = "Товарообіг факт. 'Галактон'")
plt.plot(cvar,percent,label = "Відсотки виконання 'Галактон'")
plt.plot(cvar,prod_plan,label = "Продуктивність план. 'Галактон'")
plt.plot(cvar,prod_fact,label = "Продуктивність факт. 'Галактон'")
plt.xlabel("Квартал")
plt.legend()
plt.grid(True)

Plan = [43102.60,52684.50,68453.40,7529.87]
Fact = [44568.10,51825.40,68400.30,7524.03]
percent = [103.40,98.37,99.92,99.92]
prod_plan = [206.23, 263.42,345.72,345.72]
prod_fact = [235.81, 272.77,350.77,350.77]
cvar = [1,2,3,4]
plt.plot(cvar,Plan,label = "Товарообіг план. 'Універсам №1'")
plt.plot(cvar,Fact,label = "Товарообіг факт. 'Універсам №1'")
plt.plot(cvar,percent,label = "Відсотки виконання 'Універсам №1'")
plt.plot(cvar,prod_plan,label = "Продуктивність план. 'Універсам №1'")
plt.plot(cvar,prod_fact,label = "Продуктивність факт. 'Універсам №1'")
plt.xlabel("Квартал")
plt.legend()
plt.grid(True)



def showplot():
    plt.show()
