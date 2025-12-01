import matplotlib.pyplot as plt

# 1. Line Plot (Liniendiagramm)
#       Zeigt Trends, Verläufe oder Zeitreihen

x = [1,2,3,4,5]
y = [3,5,2,8,7]

# plt.plot(x,y)
# plt.title("Line Plot")
# plt.xlabel("X")
# plt.ylabel("Y")

#plt.show()

# 2. Bar Plot (Balkendiagramm)
#       Vergleicht Katagorien miteinander
cat = ["Jan","Feb","März","Apr","Mai"]
values = [3,5,2,8,7]

# plt.bar(cat,values)
# plt.title("Bar Plot")
# plt.xlabel("Kategorie")
# plt.ylabel("Wert")

# plt.show()

# 3. Scatter Plot (Streudiagramm)
#       Zeigt eine Beziehung zwischen zwei Variablen

# plt.scatter(x,y)
# plt.title("Scatter Plot")
# plt.xlabel("X")
# plt.ylabel("Y")

# plt.show()

# 4. Histogram
#   Zeigt die Verteilung numerischer Daten

import numpy as np

daten = np.random.randn(500)

# plt.hist(daten, bins=30)
# plt.title("Histogramm")
# plt.xlabel("Werte")
# plt.ylabel("Häufigkeit")

# plt.show()


# 5. Boxplot
#   Zeigt Verteilungen , Median, Quartile

# plt.boxplot(daten)
# plt.title("Boxplot")
# plt.ylabel("Wert")

# plt.show()

# 6. Pie Chart (Kreisdiagramm)
#   Zeigt Anteile (z.B. Marktanteile )

# lable = ["A","B","C"]
# size = [20,50,30]

# plt.pie(size, labels=lable)
# plt.title("Pie Chart")
# plt.show()

# 7. Subplots - (mehrere Diagramme in einer Figur)
#   Mehrere Visualisierung nebeneinander

# fig, axs = plt.subplots(1,2)

# axs[0].plot(x,y)
# axs[0].set_title('Line')

# axs[1].bar(x,y)
# axs[1].set_title("Bar")

# plt.show()


# 8. Matplotlib + Pandas
import pandas as pd

# df = pd.DataFrame({
#     "mpg":[18,15,36,30,22],
#     "hp":[130,165,88,70,98]
#     })

# plt.scatter(df["hp"],df["mpg"])
# plt.xlabel("Horsepower")
# plt.ylabel("MPG")
# plt.title("HP vs MPG")
# plt.show()

# 9. Achsen, Title, Grid & Limits

# plt.plot(x,y)
# plt.title("Title")
# plt.xlabel("X-Achse")
# plt.ylabel("Y-Achse")
# plt.xlim(0,6)
# plt.ylim(0,10)
# plt.show()

# 10. Annotations - Datenpunkte beschriften
plt.plot(x,y)
for xi,yi in zip(x,y):
    plt.annotate(f"{yi}",(xi,yi))

plt.title("Plot mit Annotation")
plt.show()