from load_csv import load
import matplotlib.pyplot as plt


def main():
    doc = load("data.csv")
    km = doc["km"]
    price1 = doc["price"]
    mileage1 = list(km)
    mileage = [x / 1000 for x in mileage1]
    price = list(price1)

    learningRate = 0.0001
    m = len(price)
    theta0 = 0
    theta1 = 0
    print("m :", m)
    o = 0
    epsilon = 0.00001  # tolérance pour la convergence
    tmpTheta0 = 0
    tmpTheta1 = 0
    somme1 = 0
    somme2 = 0
    while o == 0 or (abs(tmpTheta0) > epsilon or abs(tmpTheta1) > epsilon):
        # print("o = ", o, ", theta0 = ", theta0, ", theta1 =", theta1)
        i = 0
        somme1 = 0
        while i <= (m-1):
            estimatePrice = theta0 + (theta1 * mileage[i])
            somme1 += (estimatePrice - price[i])
            i += 1
        i = 0
        somme2 = 0
        while i <= (m-1):
            estimatePrice = theta0 + theta1 * mileage[i]
            somme2 += (estimatePrice - price[i]) * mileage[i]
            i += 1
        tmpTheta0 = learningRate * (1/m) * somme1
        tmpTheta1 = learningRate * (1/m) * somme2
        # print("somme1 :", somme1, ", somme2 :", somme2)
        # print("tmpTheta1 :", tmpTheta1, ", tmpTheta0 :", tmpTheta0)
        theta0 = theta0 - tmpTheta0
        theta1 = theta1 - tmpTheta1
        # print("-------------------------")
        # print()
        o += 1
    print("somme1 :", somme1, ", somme2 :", somme2)
    print("tmpTheta1 :", tmpTheta1, ", tmpTheta0 :", tmpTheta0)
    print("FIN : theta1 :", theta1, ", theta0 :", theta0)
    x = 185530 / 1000
    y = theta0 + (theta1 * x)
    print("une voiture a ", x, "km, coutera :", y)
    print("resultat attendu : 4450")
    x2 = [0, 100, 250]           # en milliers, pour correspondre à ton modèle
    y2 = [theta0 + theta1 * x1 for x1 in x2]

    # Pour l'affichage, mettre l'axe X en km
    plt.plot(km, price1, 'o')                       # points réels
    plt.plot([xi*1000 for xi in x2], y2, color="red") # droite de régression
    plt.xlabel("price")
    plt.ylabel("km")
    plt.show()
    plt.close()

    # while o <= 5:
    #     print("o = ", o, ", theta0 = ", theta0, ", theta1 =", theta1)
    #     i = 0
    #     somme1 = 0
    #     while i <= (m-1):
    #         estimatePrice = theta0 + (theta1 * mileage[i])
    #         somme1 += (estimatePrice - price[i])
    #         i += 1
    #     i = 0
    #     somme2 = 0
    #     while i <= (m-1):
    #         estimatePrice = theta0 + theta1 * mileage[i]
    #         somme2 += (estimatePrice - price[i]) * mileage[i]
    #         i += 1
    #     tmpTheta0 = learningRate * (1/m) * somme1
    #     tmpTheta1 = learningRate * (1/m) * somme2
    #     print("somme1 :", somme1, ", somme2 :", somme2)
    #     print("tmpTheta1 :", tmpTheta1, ", tmpTheta0 :", tmpTheta0)
    #     theta0 = theta0 - tmpTheta0
    #     theta1 = theta1 - tmpTheta1
    #     print("-------------------------")
    #     print()
    #     o += 1
    # print("FIN : theta1 :", theta1, ", theta0 :", theta0)
    # x = 185530 / 1000
    # y = theta0 + (theta1 * x)
    # print("une voiture a ", x, "km, coutera :", y)
    # print("resultat attendu : 4450")
    # x2 = [0, 100, 250]           # en milliers, pour correspondre à ton modèle
    # y2 = [theta0 + theta1 * x1 for x1 in x2]



if __name__ == "__main__":
    main()