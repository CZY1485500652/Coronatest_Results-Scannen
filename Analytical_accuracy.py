import time as t
import numpy as np
from time import sleep
from KNN_algorithm import KNN
import matplotlib.pyplot as plt
from Read_Image import Read_Image_Feature



start = t.time()

print("_________________________________________________________________________________________________________________")
print("Start to Analysing accuray ")
time = [5, 4, 3, 2, 1, 0]

for x in time:
    print("Counting : " + str(x))
    sleep(1)

print()
X_Negatief = [9.28, 9.3, 14.2, 13.88, 17.380000000000003, 13.639999999999999, 15.64, 15.740000000000002, 8.0, 9.62, 13.56, 11.98, 10.22, 10.100000000000001, 7.46, 10.100000000000001, 8.98, 10.66, 9.94, 11.08, 8.42, 10.0, 9.700000000000001, 10.18, 10.32, 9.84, 10.459999999999999, 8.459999999999999, 10.0, 10.94]
Y_Negatief = [0.0, 0.0, 4.859999999999999, 0.04, 0.0, 0.0, 2.42, 0.0, 0.0, 0.08, 0.06, 0.0, 0.22, 0.0, 0.0, 0.27999999999999997, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.24, 0.0, 2.2399999999999998, 0.0, 1.78]

X_Positief = [14.26, 16.14, 20.96, 14.34, 13.54, 30.620000000000005, 9.76, 22.58, 9.26, 9.78, 19.66, 12.22, 29.459999999999997, 14.280000000000001, 12.78, 13.22, 12.4, 13.34, 12.1, 11.940000000000001, 11.06, 12.16, 9.879999999999999, 14.299999999999999, 12.1, 12.86, 10.280000000000001, 10.0, 10.5, 13.459999999999999]
Y_Positief = [14.66, 18.8, 22.28, 10.74, 7.779999999999999, 16.42, 5.54, 17.299999999999997, 8.66, 1.3599999999999999, 16.38, 7.6, 16.2, 14.12, 3.8, 9.24, 8.04, 13.44, 1.82, 1.26, 11.16, 9.22, 0.26, 15.879999999999999, 1.28, 6.74, 0.0, 0.04, 0.9199999999999999, 4.38]

X_Onbekend = [0.33999999999999997, 0.0, 0.7000000000000001, 0.0, 0.72, 0.04, 0.18, 0.0, 0.2, 0.0, 0.0, 0.04, 1.58, 0.32, 0.33999999999999997, 0.0, 0.45999999999999996, 0.13999999999999999, 0.02, 0.1, 0.52, 0.0, 0.88, 0.08, 0.0, 2.2800000000000002, 0.18, 0.42, 0.06, 0.98]
Y_Onbekend = [11.799999999999999, 16.7, 16.06, 15.52, 13.86, 11.62, 11.559999999999999, 11.0, 10.780000000000001, 12.02, 8.7, 14.46, 17.419999999999998, 12.6, 13.56, 15.02, 14.499999999999998, 9.32, 12.0, 10.72, 15.879999999999999, 10.16, 17.68, 11.3, 12.24, 17.36, 17.94, 12.86, 16.919999999999998, 17.2]

True_Resultaten = [
               'Onbekend', 'Positief', 'Onbekend', 'Onbekend', 'Negatief', 'Negatief', 'Positief', 'Positief', 'Positief', 'Positief',
               'Positief', 'Negatief', 'Negatief', 'Onbekend', 'Positief', 'Positief', 'Positief', 'Positief', 'Positief', 'Onbekend',
               'Onbekend', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Negatief', 'Positief', 'Negatief', 'Negatief'
             ]

Train_Total = [x for x in range(1, 31)]



for k in range(6):

    print("K =", (k+1))
    Procenten = []

    # x betekent aantal van de training data
    for x in range(1, 31):
        Resultaten = []

        # betekent file van test1 - test 30
        for y in range(1, 31):
            filename = "Test/T-" + str(y) + ".jpeg"
            XY = Read_Image_Feature(filename)
            x_t, y_t = XY[0], XY[1]
            r = KNN(X_Negatief[0:x + k], Y_Negatief[0:x + k], X_Positief[0:x + k], Y_Positief[0:x + k],
                    X_Onbekend[0:x + k], Y_Onbekend[0:x + k], (k+1), x_t, y_t)
            Resultaten.append(r)

        print(str(x) + " : " + str(Resultaten))
        true = 0

        # bij c staat elkeer keer vergelijken met True resultaten
        for c in range(30):
            if str(Resultaten[c]) == str(True_Resultaten[c]):
                true += 1

        correct = int(true) / 30 * 100
        Procenten.append(correct)

    print(Procenten)
    print()

    poly_regre = np.poly1d(np.polyfit(Train_Total, Procenten, 3))

    plt.subplot(2, 3, (k + 1))
    plt.scatter(Train_Total, Procenten)
    plt.plot(Train_Total, poly_regre(Train_Total), label='Polynomial Regression', c='red')
    k_times = k + 1
    plt.title("K = " + str(k_times))

    l = "k = " + str(k_times)

    plt.scatter(Train_Total, Procenten, label=str(l), c='blue')
    plt.xlabel('Aantal van Train data')
    plt.ylabel('Procenten van Accuracy')
    plt.legend()

print()
print("End of Analysing accuracy")
print("_________________________________________________________________________________________________________________")

for x in time:
    print("Plot figures : " + str(x))
    sleep(1)

end = t.time()

print()
print("Totale time : ", (end-start))

plt.show()


