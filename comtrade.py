import csv
import matplotlib.pyplot as plt

#Import and format csv file.
filename = 'data/comtrade.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    #Get exports from this file.
    trade_values = []
    for row in reader:
        trade_value = int(row[31])
        trade_values.append(trade_value)

#Plot the high trade values.
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(trade_values, c='green')

#Format plot.
ax.set_title("Global Trade Value 2019", fontsize=20)
ax.set_xlabel('Country Code', fontsize=16)
ax.set_ylabel("(In Trillions)", fontsize=16)

plt.show()
