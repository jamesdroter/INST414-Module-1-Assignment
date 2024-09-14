import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

baseball_df = pd.read_csv("savant_stats.csv")

##Exit Velocity/ERA Scatterplot
sns.lmplot(x="exit_velocity_avg", y="p_era", data=baseball_df)
xy_1 = sns.scatterplot(x="exit_velocity_avg", y="p_era", data=baseball_df)
xy_1.set_title("Correlation Between Exit Velocity and ERA")
xy_1.set_xlabel("Exit Velocity Average")
xy_1.set_ylabel("Earned Run Average")
r1 = stats.pearsonr(baseball_df["p_era"], baseball_df["exit_velocity_avg"])
print(r1)


##Launch Angle/ERA Scatterplot
sns.lmplot(x="launch_angle_avg", y="p_era", data=baseball_df)
xy_2 = sns.scatterplot(x="launch_angle_avg", y="p_era", data=baseball_df)
xy_2.set_title("Correlation Between Launch Angle Average and ERA")
xy_2.set_xlabel("Launch Angle Average")
xy_2.set_ylabel("Earned Run Average")
r2 = stats.pearsonr(baseball_df["p_era"], baseball_df["launch_angle_avg"])
print(r2)


##Hard Hit %/ERA Scatterplot
sns.lmplot(x="hard_hit_percent", y="p_era", data=baseball_df)
xy_3 = sns.scatterplot(x="hard_hit_percent", y="p_era", data=baseball_df)
xy_3.set_title("Correlation Between Hard Hit Percenatage and ERA")
xy_3.set_xlabel("Hard Hit Percentage")
xy_3.set_ylabel("Earned Run Average")
r3= stats.pearsonr(baseball_df["hard_hit_percent"], baseball_df["p_era"])
print(r3)


##On-Base + Slugging %/ERA Scatterplot
sns.lmplot(x="on_base_plus_slg", y="p_era", data=baseball_df)
xy_4 = sns.scatterplot(x="on_base_plus_slg", y="p_era", data=baseball_df)
xy_4.set_title("Correlation Between OPS and ERA")
xy_4.set_xlabel("OPS")
xy_4.set_ylabel("Earned Run Average")
r4= stats.pearsonr(baseball_df["on_base_plus_slg"], baseball_df["p_era"])
print(r4)

plt.show()