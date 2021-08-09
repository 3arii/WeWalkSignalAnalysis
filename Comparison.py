
import numpy as np
from matplotlib import pyplot as plt

x, y = np.loadtxt("AccDataBroken.txt", unpack=True, delimiter=",")

lower_list = []
higher_list = []

# Take m as slope and b as intercept
m, b = np.polyfit(x, y, 1)

plt.plot(x, y)
plt.plot(x, m*x + b)

best_fit_line = np.mean(m*x + b)

for num in y:
  if num > best_fit_line:
    higher_list.append(num)
  else:
    lower_list.append(num)

mean_higher_list = sum(higher_list) / len(higher_list)
mean_lower_list = sum(lower_list) / len(lower_list)

differences = mean_higher_list - mean_lower_list

if differences < 0.01 and differences > 0.002:
  print("Faulty WeWalk.")
else:
  print("Good WeWalk.")

print(differences)

def get_differences(number):
  if differences > 0.01 and differences < 0.002:
    print("Soultion solved")

plt.show()
