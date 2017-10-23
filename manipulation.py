# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.style.use('ggplot')

# plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False

# data directory
data_dir = "../data/零调数据"


# df = pd.read_csv("grade.csv")
# print(df)
# df["grade"].plot(kind="bar")
# plt.savefig("hehe.png")


# df4 = pd.DataFrame({'wyy': np.random.randn(1000) + 1,
#                     'zyx': np.random.randn(1000),
#                     'yx': np.random.randn(1000) - 1},
#                    columns=['wyy', 'zyx', 'yx'])


# df = pd.read_csv("grade.csv")
# print(df)
# df["grade"].plot(kind="bar")
# plt.savefig("hehe.png")


# df4.plot(kind='hist', alpha=0.5)
# plt.savefig("1.png")


df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot(kind='hexbin', x='a', y='b', gridsize=25)
plt.savefig("2.png")
