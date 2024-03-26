import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Africa E-Mobility Raw Data.csv")

#EV Readiness graph
x = data["Country"]
y = data["EV Readiness(%)"]
plt.figure(figsize=(10, 10)) 
plt.plot(x,y, color = "red")
plt.xlabel("Country")
plt.ylabel("EV Readiness(%)")
plt.xticks(rotation=90)
plt.title("EV readiness distribution by country", fontsize = 20)
plt.savefig('plot.png')
plt.show()

#Total EVs graph
a = data["Total EVs"]
plt.figure(figsize=(10, 10)) 
plt.bar(x,a)
plt.ylabel("EV Distribution")
plt.xlabel("Country")
plt.xticks(rotation=90)
plt.title("EV distribution by country", fontsize = 20)
plt.savefig("plot2.png")
plt.show()

#Comparison of the EVs
d = ["2W/3W", "4W/LDW", "Buses"]
c = data[d]
plt.figure(figsize=(10, 10)) 
for i, col in enumerate(d):
    plt.scatter(c[col], x, label=f'{col}')
plt.ylabel("Country")
plt.xlabel("EV Distribution")
plt.xticks(rotation=90)
plt.legend(title="Legend", loc="best")
plt.title("EV distribution by type", fontsize = 20)
plt.savefig('plot3.png')
plt.show()

#No of charging stations
b = data["Number of companies"]
plt.figure(figsize=(10, 10)) 
plt.barh(x,b, color = 'teal')
plt.xlabel("Number of companies")
plt.ylabel("Country")
plt.xticks(rotation=90)
plt.title("Charging Stations Distribution", fontsize = 20)
plt.savefig("plot4.png")
plt.show()

#Regions of Africa
e = data["Region"]
f = data["Total EVs"]
grouped_data = data.groupby('Region')
sums = grouped_data["Total EVs"].sum()
label = sums.index
plt.figure(figsize=(10, 10)) 
plt.pie(sums, labels = label, autopct='%1.1f%%', startangle=140, labeldistance=1.07)
plt.title("EV distribution by region", fontsize = 30)
plt.axis('equal') 
plt.savefig("plot5.png")
plt.show()





