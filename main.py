import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p13 = (87 + 81 + 75) / 3
p14 = ( 81 + 75 + p13) / 3
p = np.array(list([92, 85, 80, 87, 79, 82, 89, 83, 80, 87, 81, 75, p13, p14]))
s = np.array(list(range(1, len(p)+1)))
data = {"s" : s, "p" : p}
df = pd.DataFrame(data=data, index=list(range(1, len(p)+1)))
df = df["p"].to_frame()
df["MA3"] = df["p"].rolling(3).mean().shift(1)
df["er3"] = np.power((df["p"] - df["MA3"]), 2)
df["MA4"] = df["p"].rolling(4).mean().shift(1)
df["er4"] = np.power((df["p"] - df["MA4"]), 2)
df["MA5"] = df["p"].rolling(5).mean().shift(1)
df["er5"] = np.power((df["p"] - df["MA5"]), 2)
df["MA6"] = df["p"].rolling(6).mean().shift(1)
df["er6"] = np.power((df["p"] - df["MA6"]), 2)
MSE3 = df["er3"].mean()
MSE4 = df["er4"].mean()
MSE5 = df["er5"].mean()
MSE6 = df["er6"].mean()
print(f"MSE3 : {MSE3}\nMSE4 : {MSE4}\nMSE5 : {MSE5}\nMSE6 : {MSE6}\n")
print(df)
df[["p", "MA3"]].plot(label="MA")
plt.show()
