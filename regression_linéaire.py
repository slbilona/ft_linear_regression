from load_csv import load
import matplotlib.pyplot as plt
from ft_statistics import functions
from math import sqrt


def calculRegressionLineaire(kmList : list, priceList : list) -> list:
    # x = price, y = km
    print("pricelist = ", priceList)
    moyX = functions.mean(priceList)
    moyY = functions.mean(kmList)
    sumXY = [x * y for x, y in zip(priceList, kmList)]
    moyXY = functions.mean(sumXY)
    # moyXCarré =
    # moyYCarré =
    varX = functions.var(priceList)
    varY = functions.var(kmList)
    
    a = (moyXY - moyX * moyY) / varX
    print(a, " = (", moyXY, " - (", moyX, " * ", moyY, ")) / ", varX)
    b = moyY - (a * moyX)
    print(b, " = ", moyY, " - (", a, " * ", moyX, ")")
    r = (moyXY - moyX * moyY) / (sqrt(varX) * sqrt(varY))
    print("r =", r)
    return [a, b]


def main():
    try:
        doc = load("data.csv")
        print(doc)
        print("doc[\"km\"] :", doc["km"])
        print("doc[\"price\"] :", doc["price"])
        km = doc["km"]
        price = doc["price"]

        kmList = list(km)
        priceList = list(price)
        result = calculRegressionLineaire(kmList, priceList)
        a = result[0]
        b = result[1]
        x = [3000, 9000]
        y = [((a * x1) + b) for x1 in x]
        print(y)
        plt.plot(price, km, 'o')
        plt.plot(x, y, color="red")
        plt.xlabel("km")
        plt.ylabel("price")
        plt.show()
        plt.close()
    except Exception as e:
        print("error: ", e)



if __name__ == "__main__":
    main()