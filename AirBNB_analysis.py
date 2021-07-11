# =============================================================================
# AirBNB - Ney York City
# Bradley Kurit

# =============================================================================

# =============================================================================
# Introduction
# Since 2008, guests and hosts have used Airbnb to expand on traveling
# possibilities and present a more unique, personalized way of experiencing the
# world. This dataset describes the listing activity and metrics in NYC, NY
# for 2019. This data file includes all needed information to find out more
# about hosts, geographical availability, necessary metrics to make predictions
# and draw conclusions. I suggest you open the data file and look through the
# data.
#
# In general, we are interested in answering the following questions:
# - What can we learn about different hosts and areas?
# - What can we learn from predictions? (ex: locations, prices, reviews, etc)
# - Which hosts are the busiest and why?
# - Is there any noticeable difference in traffic among different areas and
#   what could be the reason for it?
#
# These might be the initial questions that pop into your head when trying to
# understand the data. After thinking about our problem more generally we can
# dive into the details.
# =============================================================================

# =============================================================================
# Data description
# The dataset includes the following variables for each entry (each of 49,000
# listings):
# - name (name of the apartment)
# - host id (ID set by Airbnb)
# - host name
# - neighborhood group (Manhattan, Brooklyn, ...)
# - neighborhood
# - latitude (north-south direction, y-axis)
# - longitude (east-west direction, x-axis)
# - room type
# - price (price per night in USD)
# - minimum nights (minimum amount of nights the guest has to stay)
# - number of reviews
# - last review (date of the last review)
# - reviews per month (average number of reviews per month)
# - calculated host listing cost (the cost hosts have to pay for their listing)
# - availability 365 (how many days per year is the listing available)
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# Exercise 1 - Data Collection and Cleaning
# =============================================================================

# =============================================================================
# Part 1
# - Import the dataset for the file "AB_NYC_2019.csv".
# =============================================================================

# df = pd.read_csv("/users/kurit/downloads/AB_NYC_2019.csv")

# # =============================================================================
# # Part 2
# # - Deal with any Null values in the table.
# # - Are there any incorrect values in the table?
# # - Write how you cleaned the data and why have you've chosen this route.
# #   A: The reviews per month were set to a zero data point and the last review 
# #      was set to a 01/01/2000 date as it would be easy to differentiate between 
# #      the data.
# # - Is there any pattern with missing or incorrect values? Can you explain the
# #   origin of the errors?
# #   A: If there was no last review there isn't a reviews_per_month value. This
# #      happens because the listing doesn't have any reviews.
# # =============================================================================

# df = pd.read_csv("/users/kurit/downloads/AB_NYC_2019.csv")
# df["last_review"].fillna("01/01/1900",inplace=True)
# df["reviews_per_month"].fillna(0,inplace=True)
# df["last_review"] = pd.to_datetime(df["last_review"])
# df.to_csv('cleaned_data1.csv')

# =============================================================================
# Part 3
# - In this analysis we are interested in the profitability of each listing.
#   Of course we cannot determine the true profitability since we don't know
#   all the costs, the number of booked night, but we can use the given data
#   to create a metric that resembles profitability.
# - Create a new column named profitability that is calculated with the 
#   following equation
#       profitability = price * avaliability_365 * (1 + reviews_per_month)
# - Describe why you think this formula is a good representation of profitability
#   and suggest how we could improve it, what data we would need.
#   A: We presumed that profitability is proportional to the price of the listing,
#      the number of days available and the number of reviews per month. We added
#      plus 1 to the reviews term since profitable listings don't have to have
#      any review, otherwise the profitability would have been zero. To improve it
#      we would need data on total cost of accommodation, AriBNB fees, number
#      of reservations, total revenue.
# =============================================================================

# profitability = []
# for i in df.index:
#     listing = df.loc[i]
#     profitability.append(listing["price"]*listing["availability_365"]*(1+listing["reviews_per_month"]))
# df["profitability"] = profitability
# print(df["profitability"])


# =============================================================================
# Part 4
# - Save the cleaned version to a new file, so that you don't have to repeat 
#   this step every time.
# =============================================================================


# df.to_csv("/users/kurit/downloads/AB_NYC_2019_cleaned.csv")

# =============================================================================
# Exercise 2 - Analysis
# =============================================================================
df = pd.read_csv("/users/kurit/downloads/cleaned_data.csv")#/users/kurit/downloads/cleaned_data.csv")
 
# =============================================================================
# Part 1
# - Compare the price distribution in each neighborhood group. Since we are
#   interested in the distribution it means we will be using a histogram.
# - To compare two histograms calculate the mean and standard deviation of
#   each histogram.
# - What can we learn from creating these plots?
#   A: By analysing the mean and standard deviation can conclude that Manhattan
#      is the most expensive with highest range of listing prices. Looking at
#      Bronx and Queens we see the lowest average price with very narrow span
#      of prices. 
# =============================================================================


# # Print all the different neighborhood groups
# print(df.groupby("neighbourhood_group").count().index)  # Print all the neighborhood groups.

# # Graph of price distribution
# i = 1
# plt.suptitle("Price Distribution")
# for group in df.groupby("neighbourhood_group").count().index:
#     plt.subplot(3,2,i)
#     plt.hist(df[df["neighbourhood_group"] == group]["price"], bins=np.linspace(0, 750, 50))
#     plt.title("Price distrabution in {}".format(group))
#     plt.xlabel("Price")
#     plt.ylabel("Number of listings")
#     i += 1
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.savefig("price_distribution.pdf")
# plt.show()  

# # Mean and standard deviation for each group.
# print(df.groupby("neighbourhood_group").mean()["price"])
# print(df.groupby("neighbourhood_group").std()["price"])
# Group            Mean           Std
# Bronx             87.496792     106.709349
# Brooklyn         124.383207     186.873538
# Manhattan        196.875814     291.383183
# Queens            99.517649     167.102155
# Staten Island    114.812332     277.620403

# =============================================================================
# Part 2
# - Which room types are most profitable and which are the most common?
#   A: The most profitable room would be the entire house and then the private room. The most common room would be the enitre house followed by the orivate room and then shared room
# =============================================================================

# Profitability Distribution per Room Type
# i = 1
# plt.suptitle("Profitability Distribution per Room Type")
# for room in df.groupby("room_type").mean().index:
#     plt.subplot(3,1,i)
#     i += 1
#     plt.hist(df[df["room_type"] == room]["profitability"], bins=np.linspace(1, 100000, 100))
#     plt.xlabel("Profitability")
#     plt.ylabel("Number of listings")
#     plt.title("Profitability Histogram of {}".format(room))
# plt.show()

# # Most common
# print(df.groupby("room_type").count()["price"])
# # Entire home/apt    25409
# # Private room       22326
# # Shared room         1160

# # Bar chart of average price for all room types
# plt.bar(df.groupby("room_type").mean().index, df.groupby("room_type").mean()["price"])
# plt.title('Average price of different types of rooms')
# plt.ylabel('Price [$]')
# plt.xlabel('Type of room')
# plt.show()

# =============================================================================
# Part 3
# - Create a scatter plot/map of all the listings where the color of the point
#   is proportional to the price. 
# - Optional: you can overlap the plot of the picture of New York using imshow().
# - What can this plot tell you about price distribution and listing density?
#   A: This heat map shows that Manhattan has the more expensive rooms as well 
#      as the most availability of the New York cities.
# =============================================================================

# df = df[df["price"] < 500]      # We limit the prices so that we can see the smaller differences between points (we remove the extremes)
# nyc_img = plt.imread("New_York_City.png", 0)
# plt.imshow(nyc_img, zorder = 0, extent = [-74.258, -73.7, 40.49,40.92])   # Scales the image to match with coordinates
# ax = plt.gca()    # gets the axes from the current figure
# df.plot(kind='scatter', x='longitude', y='latitude', c='price', ax = ax, cmap=plt.get_cmap('jet'), colorbar=True, alpha=0.4, figsize=(10,8))
# plt.title("Heatmap of listing price in New York")
# plt.show()

# =============================================================================
# Part 4
# - What does an average listing look like?
# - For the variables that you can't calculate the average (like room type, ...)
#   create a pie chart or just look at the count for each type.
#   A:
# =============================================================================

# print(df.mean())
# # price                             $152.72
# # minimum_nights                    7.0
# # number_of_reviews                 23.3 reviews
# # reviews_per_month                 1.09 reviews/month
# # calculated_host_listings_count    $7.14
# # availability_365                  113 days
# # profitability                     42794.07
plt.figure(figsize=(10,10))
plt.suptitle("Room Types and Neighbourhood Groups")
plt.subplot(2,2,1)
print(df.groupby("room_type").count()["price"])
plt.pie(df.groupby("room_type").count()["price"], labels = df.groupby("room_type").mean().index, explode = [0.1 for i in range(3)])
plt.title("Room Type")

# Entire home/apt    25409  52%
# Private room       22326  46%  
# Shared room         1160  2%
# print(df.groupby("neighbourhood_group").count()["price"])
plt.subplot(2,2,2)
plt.title("Neighbourhood Group")
plt.pie(df.groupby("neighbourhood_group").count()["price"], labels = df.groupby("neighbourhood_group").mean().index, explode = [0.1 for i in range(5)])

# Bronx             1091
# Brooklyn         20104
# Manhattan        21661
# Queens            5666
# Staten Island      373

# =============================================================================
# Part 5
# - What are the common factors of the most successful listings?
#   Since you have a lot of data points you can analyse only the top 1 %.
#   A: 
# =============================================================================

#   print(df[df["profitability"] > 100000].mean())
# price                             $337.05
# minimum_nights                    5.9 
# number_of_reviews                 55.5 reviews
# reviews_per_month                 2.6  reviews/month
# calculated_host_listings_count    17.6
# availability_365                  276.4 days
# profitability                     229464.05
plt.subplot(2,2,3)
plt.title("Room Type of Top Listings")
print(df[df["profitability"] > 100000].groupby("room_type").count()["price"])
plt.pie(df[df["profitability"] > 100000].groupby("room_type").count()["price"], labels = df.groupby("room_type").mean().index, explode = [0.1 for i in range(3)])

# Entire home/apt    4596 80%    
# Private room       1102 19%
# Shared room          33 1%
plt.subplot(2,2,4)
plt.title("Neighbourhood of Top Listings")
print(df[df["profitability"] > 100000].groupby("neighbourhood_group").count()["price"])
plt.pie(df[df["profitability"] > 100000].groupby("neighbourhood_group").count()["price"],labels = df.groupby("neighbourhood_group").mean().index, explode = [0.1 for i in range(5)])
plt.show()
plt.savefig("Top Listing chart.pdf")
# Bronx              95
# Brooklyn         1770
# Manhattan        3210
# Queens            613
# Staten Island      43

# Compare these numbers with the ones from Part 4.
# The difference between top 1% and the average listing
# price                             $184.33
# minimum_nights                    1 day less
# number_of_reviews                 32.2 reviews
# reviews_per_month                 1.5  reviews/month
# calculated_host_listings_count    10.46 
# availability_365                  163 days

