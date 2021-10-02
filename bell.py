import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

diceRes=[]
df=pd.read_csv("StudentsPerformance.csv")
score=df["math score"].tolist()
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceRes.append(dice1+dice2)

s1=sum(score)
s2=len(score)
mean=s1/s2
print(mean)
std_deviation=statistics.stdev(score)
print(std_deviation)
std_median=statistics.median(score)
std_mode=statistics.mode(score)
print(std_median)
print(std_mode)

fig=ff.create_distplot([score],["Student Scores"],show_hist=False)
first_std_start,first_std_end=mean-std_deviation,mean+std_deviation
second_std_start,second_std_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_start,third_std_end=mean-(3*std_deviation),mean+(2*std_deviation)
listOfOneStandardDev=[result for result in score if result>first_std_start and result<first_std_end]
listOf2StdDev=[result for result in score if result>second_std_start and result<second_std_end]
listOf3StdDev=[result for result in score if result>third_std_start and result<third_std_end]
print("{}% of data lies within 1 standard deviation.".format(len(listOfOneStandardDev)*100/len(score)))
print("{}% of data lies within 2 standard deviation.".format(len(listOf2StdDev)*100/len(score)))
print("{}% of data lies within 3 standard deviation.".format(len(listOf3StdDev)*100/len(score)))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end], y=[0,0.17],mode="lines",name="Standard Deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end], y=[0,0.17],mode="lines",name="Standard Deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end], y=[0,0.17],mode="lines",name="Standard Deviation 3 end"))
fig.show()