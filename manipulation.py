# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import shutil
import sys
import time
matplotlib.style.use('ggplot')

# plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False


def frc(std, side, how):
    return ("L_F{std}H_{side}RLFCFBK{how}"
            .format(std=std, side=side, how=how))


def pos(std, side, access):
    return ("L_F{std}H_{side}{access}POSFBK"
            .format(std=std, side=side, access=access))


def slp(side, access, how, times):
    return ("k_{side}_{access}_{how}_{times}"
            .format(side=side, access=access, how=how, times=times))


def progressbar(i):
    """ 小型的进度条 """
    sys.stdout.write('第{0}机架计算中！- 总共7机架\r'.format(i + 1))
    sys.stdout.flush()


# --- setup para ---
# data directory
root_dir = "../data/零调数据"

last_num_list = [-1, -2, -3]
times_id_list = ["A", "B", "C", "D", "E", "F"]
std_list = [1, 2, 3, 4, 5, 6, 7]
side_list = ["OS", "DS"]
access_list = ["ENT", "EXT"]
how_list = ["LC", "PT"]
level_line = 4000


last_num = -1

summary = pd.DataFrame()
last_date = os.listdir(root_dir)[last_num]
data_dir = "/".join([root_dir, last_date])
for times_id in times_id_list:
    print(times_id)
    file_name = [x for x in os.listdir(data_dir) if times_id in x][0]
    df = pd.read_csv("/".join([data_dir, file_name]))
    for std in std_list:
        df = df.loc[df[frc(std, "OS", "LC")] > level_line]
        for side in side_list:
            for access in access_list:
                for how in how_list:
                    pos_size = df[pos(std, side, access)].shape[0]
                    frc_size = df[frc(std, side, how)].shape[0]
                    if ((pos_size != 0) and (frc_size != 0) and
                            (pos_size == frc_size)):
                        summary[std, slp(side, access, how, times_id)] = (
                            np.polyfit(df[pos(std, side, access)],
                                       df[frc(std, side, how)], 1)[0]
                        )
                    else:
                        summary[std, slp(side, access, how, times_id)] = 0


summary.to_excel("result.xlsx")
# first a as an example

# def
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


# df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
# df.plot(kind='hexbin', x='a', y='b', gridsize=25)
# plt.savefig("2.png")
