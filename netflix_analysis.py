#!/usr/bin/env python
# coding: utf-8


#import modules:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#define functions for plots:

#define function for pie:
def pie_MvsTv(pie_size,pie_x,pie_l,pie_pct,pie_title):
    '''Pie charts can be helpful for showing the relationship of parts to the 
       whole when there are a small number of levels and we have only two type 
       of the title to shows here so pie chart is perfectly suitable. 
    '''
    plt.figure(figsize=pie_size)
    plt.pie(x=pie_x,labels=pie_l,autopct=pie_pct)
    plt.legend()
    plt.title(pie_title)
    plt.savefig("pie_fig")
    plt.show()

#define function for barplot:
def barplot_mvstv(x,y,xbar_lab,ybar_lab,title):
    sns.barplot(x=x,y=y)
    plt.xlabel(xbar_lab)
    plt.ylabel(ybar_lab)
    plt.title(title, fontsize=15)
    plt.savefig("barplot_fig")
    plt.show()
    
#define function for linegraph:
def linegraph(data1,data2,xline_lab,yline_lab,title):
    plt.figure(figsize=(12,4))
    plt.xlabel(xline_lab, fontsize=12)
    plt.ylabel(yline_lab, fontsize=12)
    plt.title(title)
    sns.lineplot(x=x,y=y)
    plt.savefig("linegraph_fig")
    plt.show()

#define function for multilinegraph:
def multiline(size,x1,y1,l1,x2,y2,l2,xmline_lab,ymline_lab,title):
    plt.figure(figsize=size)
    plt.plot(x1,y1,linewidth=3,label=l1)
    plt.plot(x2,y2,linewidth=3,label=l2)
    plt.legend()
    plt.title(title)
    plt.xlabel(xmline_lab, fontsize=12)
    plt.ylabel(ymline_lab, fontsize=12)
    plt.savefig(title)
    plt.show()
    


#read_file:
netflix_df = pd.read_csv("netflix_titles.csv", sep=',')


#data preprocessing

#new dataframe for group by year of tvshows and movies and count them:
netflix_dates = netflix_df[['type', 'date_added']].copy() #make new data frame for store dates and type 

#Convert argument to datetime and to find the years present in the DatetimeIndex.
netflix_dates['date_added'] = pd.to_datetime(netflix_dates['date_added'])  
netflix_dates['year_added'] = pd.DatetimeIndex(netflix_dates['date_added']).year 

#count movies and tv shows added in particular year:
count = netflix_dates.groupby(['year_added', 'type']).count().rename(columns={'date_added': 'count'})
count.reset_index(inplace=True)
count_tvshow = count[count['type']=='TV Show']
count_movie = count[count['type']=='Movie']

#count of total movies and tv shows
total_tvshows = count_tvshow['count'].sum()
total_movies = count_movie['count'].sum()
print('Total Movies:',total_movies)
print('Total Tv Shows:',total_tvshows)

print(netflix_df.head())
netflix_df.head()


#pie chart

#showing data for tv shows and movie count with help of pie:
pie_size = (8,6)
pie_x = netflix_df['type'].value_counts()
pie_l = ['Movie','TV Show']
pie_pct = '%0.1f%%'
pie_title ="Does Netflix have more TV Shows or Movies?"

#produce pie chart by predefine function:
pie_MvsTv(pie_size,pie_x,pie_l,pie_pct,pie_title)

'''Pie charts can be helpful for showing the relationship of parts to the whole
 when there are a small number of levels and we have only two type of the title
 to shows here so pie chart is perfectly suitable. 
'''

#bargraph:

#cont of movies and tv shows by country where release:
top_country = netflix_df['country'].value_counts().head(5)

#top country distribution for netflix content:
x = top_country.index
y = top_country.to_list()

#produce bargraph by predefine function:
barplot_mvstv(x,y,"Countries","count","Top Country where the movie / Tv show is released")

'''A bar chart is used when you want to show a distribution of data points or 
perform a comparison of metric values across different subgroups of your data 
so here its perfectly fit for showing top 5 country distrubuition by realese
'''


#line graph:

#showing releas rate of netflix content using line graph:

rate_count = netflix_df['release_year'].value_counts()
x = rate_count.index
y = rate_count.values
#produce a line graph by predefine function:
linegraph(x, y, "years", "count","RELEASE RATEs")
'''
Line graphs are used to track changes over short and long periods of time.
here we showing the release rate of movies and tv shows over the years.
'''

#multiline graph:

#showing numbers of tvshows and movies has been added in over the years using line graph:\
size = (10,6)
x1 = count_tvshow['year_added']
y1 = count_tvshow['count']
x2 = count_movie['year_added']
y2 = count_movie['count']
l1 = 'TV Show'
l2 = 'Movie'

title = 'Count of TV Show and Movie Based On The Year When They Are Added'

#produce multiline graph by predefine function:
multiline(size,x1,y1,l1,x2,y2,l2,"years","count",title)
'''
Line graphs are used to track changes over short and long periods of time.
so here its best match for showing tv shows and movies count charges over the 
Years.
'''