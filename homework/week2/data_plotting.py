import matplotlib.pyplot as plt
import pandas as pd
url = 'https://raw.githubusercontent.com/ipozdeev/it-skills-for-research/master/data/coding-environment-exercise.csv'
df = pd.read_csv(url)

# make up some data
x = df.date
y = df.value

# plot
plt.plot(x,y)
plt.gcf().autofmt_xdate()

plt.show()