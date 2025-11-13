#MapPlot.py
#Name: Kylie Krusemark
#Date: 11/14/25
#Assignment: Lab 10

import super_bowl_ads
import pandas
import matplotlib.pyplot as plt

ads = super_bowl_ads.get_advert()


brands = []
views = []

for ad in ads:
    brand = ad["Brand"]
    view = ad["Data"]["Viewership"]["Views"]
    #filter out outliers
    if view < 100000000:
        brands.append(brand)
        views.append(view)
    

df = pandas.DataFrame({"Brand": brands,
                        "Views": views})

#combine brands and average view counts
averageViews = df.groupby("Brand", as_index=False)["Views"].mean()

#sort by view count to make it look nicer
averageViews = averageViews.sort_values(by="Views", ascending=False)


graph = averageViews.plot(kind = 'bar', 
        x = 'Brand', 
        y = 'Views',
        color = "teal",
        figsize = (10,10),
        title = "Average Super Bowl Ad Views by Brand")

graph.set_xlabel("Brand")
graph.set_ylabel("Average Views")

plt.savefig('lab10')

