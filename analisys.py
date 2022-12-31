import matplotlib.pyplot as plt
import pandas
df = pandas.read_csv("dataset.csv",delimiter=" ",index_col="date_published",parse_dates=True) # usecols=["author","date_published","mood"],
arr = df.to_numpy()
print(arr.shape)
Lx = arr[:,1]


df['day of the week'] = df.index.dayofweek
df['day of the year'] = df.index.dayofyear
df['hour of the day'] = df.index.hour
df['number of the week'] = df.index.weekofyear
#df['minute of the hour'] = df.index.minute inutile a priori

print(df)

features = ["author","day of the week","day of the year","hour of the day","number of the week"]
labels = ["mood"]
df = df[labels+features]
# no need for scaling as values are between 0 and 1 already
fig = plt.figure(figsize=(18, 6))
ax = fig.add_subplot(111)
df[labels].plot(ax=ax)
plt.grid(True)
plt.show()