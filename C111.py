import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd


df = pd.read_csv("C111.csv")
data = df["Math_score"].tolist()

# code to show the plot of raw data
# fig = ff.create_distplot([data], ["temp"], show_hist=False)
# fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)
    
mean = statistics.mean(mean_list)
print("Mean of sampling distribution :-",mean )

#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)

std_deviation = statistics.stdev(mean_list)
print("Standard deviation of sampling distribution:- ", std_deviation)

f_h_stdev_start,f_h_stdev_end = mean - std_deviation,mean + std_deviation
s_h_stdev_start,s_h_stdev_end = mean - (2*std_deviation),mean + (2*std_deviation)
t_h_stdev_start,t_h_stdev_end = mean - (3*std_deviation),mean + (3*std_deviation)

print("std_dev 1: ", f_h_stdev_start,f_h_stdev_end)
print("std_dev 2: ", s_h_stdev_start,s_h_stdev_end)
print("std_dev 3: ", t_h_stdev_start,t_h_stdev_end)

#fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
#fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
#fig.add_trace(go.Scatter(x=[f_h_stdev_start, f_h_stdev_start], y=[0, 0.17], mode="lines", name="1st standard dev start"))
#fig.add_trace(go.Scatter(x=[f_h_stdev_end, f_h_stdev_end], y=[0, 0.17], mode="lines", name="1st standard dev end"))

#fig.add_trace(go.Scatter(x=[s_h_stdev_start, s_h_stdev_start], y=[0, 0.17], mode="lines", name="2nd standard dev start"))
#fig.add_trace(go.Scatter(x=[s_h_stdev_end, s_h_stdev_end], y=[0, 0.17], mode="lines", name="2nd standard dev end"))

#fig.add_trace(go.Scatter(x=[t_h_stdev_start, t_h_stdev_start], y=[0, 0.17], mode="lines", name="3rd standard dev start"))
#fig.add_trace(go.Scatter(x=[t_h_stdev_end, t_h_stdev_end], y=[0, 0.17], mode="lines", name="3rd standard dev end"))

#fig.show()

#df = pd.read_csv("C111-1.csv")
#data = df["Math_score"].tolist()

mean_1 = statistics.mean(data)
print("mean of data 1: ",mean_1)

fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_1, mean_1], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[f_h_stdev_end, f_h_stdev_end], y=[0, 0.17], mode="lines", name="1st standard dev end"))

#fig.show()

df = pd.read_csv("C111-3.csv")
data = df["Math_score"].tolist()

mean_2 = statistics.mean(data)
print("mean of data 2: ",mean_2)

fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_1, mean_1], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[f_h_stdev_end, f_h_stdev_end], y=[0, 0.17], mode="lines", name="1st standard dev end"))
fig.add_trace(go.Scatter(x=[s_h_stdev_end, s_h_stdev_end], y=[0, 0.17], mode="lines", name="2nd standard dev end"))

#fig.show()

df = pd.read_csv("C111-3.csv")
data = df["Math_score"].tolist()

mean_3 = statistics.mean(data)
print("mean of data 2: ",mean_3)

fig = ff.create_distplot([mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_3, mean_3], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[f_h_stdev_end, f_h_stdev_end], y=[0, 0.17], mode="lines", name="1st standard dev end"))
fig.add_trace(go.Scatter(x=[s_h_stdev_end, s_h_stdev_end], y=[0, 0.17], mode="lines", name="2nd standard dev end"))
fig.add_trace(go.Scatter(x=[t_h_stdev_end, t_h_stdev_end], y=[0, 0.17], mode="lines", name="3rd standard dev end"))

#fig.show()

z_sc = (mean_3-mean)/std_deviation
print(z_sc)


