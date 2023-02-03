import pandas as pd
import matplotlib.pyplot as plt
import code

ggGas = pd.read_csv('./climate-change.csv')
co2world = ggGas[ggGas['Entity']=='World']

co2world.plot(y="CO2 concentrations", 
              x='Year', 
              grid = True, 
              figsize=(20,10))

plt.xticks([-800000, -600000, -400000, -200000, 0], 
           ['800,000 BCE', '600,000 BCE', '400,000 BCE',
            '200,000 BCE','0'],
             rotation=20)

plt.ylabel("carbon dioxide level (parts per million)")
plt.xlabel("years before today (0 = 1950)")
plt.legend("")
plt.title("CO2 Concentrations")

plt.show()

#TODO: if file already exists, don't make 
#plt.savefig('images/co2world.png')

#create NH4 time graph for north america
ggGasNA = ggGas[ggGas['Entity']=='North America']

ggGasNA.plot(y="CH4 concentrations", 
              x='Year', 
              grid = False, 
              figsize=(20,10))

plt.ylabel("Methane Constrations (parts per million)")
plt.xlabel("years before today (0 = 1950)")
plt.legend("")
plt.title("North American NH4 Concentrations")

plt.show()

plt.savefig('images/nh4northAmerica.png')
