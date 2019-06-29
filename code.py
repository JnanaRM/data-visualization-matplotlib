# --------------
import pandas as pd 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
# Load the dataset and create column `year` which stores the year in which match was played
df = pd.read_csv(path)
df['year']= df.date.str.slice(start=0,stop=4)
# Plot the wins gained by teams across all seasons
res = df.groupby(['winner'])['match_code'].nunique()
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Teams')
plt.ylabel('Matches Won')
plt.show()
# Plot Number of matches played by each team through all seasons
df1=  df[['match_code','year','team1']]
df2= df[['match_code','year','team2']]
df1.rename(columns = {'team1':'team'},inplace = True)
df2.rename(columns = {'team2':'team'},inplace = True)
df3 = pd.concat([df1,df2])
#res = df3.groupby(['year','team'])['match_code'].nunique().unstack()
res = df3.groupby(['team'])['match_code'].nunique()
res.plot(kind='bar', stacked=True, figsize=(20,10))
plt.xlabel('Teams')
plt.ylabel('Matches Played')
plt.show()
# Top bowlers through all seasons
df1 = df[['year','bowler','wicket_kind']]
df1 = df1[(df.wicket_kind.notnull()) & (df.wicket_kind != 'run out')]
df1.groupby(['year','bowler'])['wicket_kind'].count()

# How did the different pitches behave? What was the average score for each stadium?
df1 = df.groupby(['match_code','venue'])[['total']].sum()/2
df1.reset_index()
df1.groupby(['venue'])['total'].mean()
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Venue')
plt.ylabel('Average Score')
plt.show()
# Types of Dismissal and how often they occur
res = df[(df.wicket_kind.notnull())]['wicket_kind'].value_counts()
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Wicket Kind')
plt.ylabel('Count')
plt.show()

# Plot no. of boundaries across IPL seasons
res = df.groupby(['year','runs'])['runs'].count().unstack()
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Boundary')
plt.ylabel('Count')
plt.show()

# Average statistics across all seasons
res = df.groupby(['year'])['match_code'].nunique()
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Year')
plt.ylabel('Mathes Played')
plt.show()

#Average Runs
df1 = df.groupby(['year','match_code'])['total'].sum().reset_index()
res = df1.groupby(['year'])['total'].mean()
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Year')
plt.ylabel('Average Runs Scored per match')
plt.show()
#average balls
df1 = df.groupby(['year','match_code'])['delivery'].count().reset_index()
res = df1.groupby(['year'])['delivery'].mean()
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Year')
plt.ylabel('Average Balls bowled per match')
plt.show()
#average runs scored per ball
df1 = df.groupby(['year'])['runs'].sum().reset_index()
df2 = df.groupby(['year'])['delivery'].count().reset_index()
df2 = df2.groupby(['year'])['delivery'].sum().reset_index()
df_join = pd.merge(df1, df2, how='inner', on = 'year')
df_join['avg run per ball'] = df_join['runs']/df_join['delivery']
res = df_join[['year','avg run per ball']]
res.set_index('year', inplace=True)
res.plot(kind='bar', figsize=(20,10))
plt.xlabel('Year')
plt.ylabel('Average Runs scored per ball')
plt.show()






