import pandas
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import matplotlib.pyplot as plt
from io import StringIO


desired_width = 320
pandas.set_option('display.width', desired_width)
pandas.set_option("display.max_columns", 15)

fl_before_cov, fl_after_cov = pandas.read_csv("otselennud.csv", delimiter=';'), \
                              pandas.read_csv("flights21.csv", delimiter=';')

with open('airports.dat', 'r', encoding='utf-8') as file:
    airports = file.read()
all_airports = pandas.read_csv(StringIO(airports), sep=",")

# Get flights that were before and that were after the Covid19
before_cov_fl = pandas.merge(all_airports, fl_before_cov, on='IATA', how='inner')
current_cov_fl = pandas.merge(all_airports, fl_after_cov, on='IATA', how='inner')

# Picture creation
plt.figure(figsize=(10, 10))
ax = plt.axes(projection=ccrs.TransverseMercator(10, approx=True))
ax.add_feature(cfeat.BORDERS, linestyle='-', alpha=4.5)
ax.add_feature(cfeat.OCEAN, facecolor=(0.1, 0.3, 0.9, 0.14))
ax.add_feature(cfeat.LAKES, facecolor=(0.1, 0.3, 0.9, 0.3))
ax.add_feature(cfeat.RIVERS)
ax.coastlines(resolution='50m')
ax.gridlines()
ax.set_extent((-7.5, 42, 34, 58), ccrs.PlateCarree())
plt.title("Julian Dinovski | Flights")

# Tallinn coordinates, starting point
tall_lon, tall_lat = 24.832800, 59.413300

for index, row in before_cov_fl.iterrows():
    iata = row['IATA']
    lat = row['Latitude']
    long = row['Longitude']

    for index2, row2 in current_cov_fl.iterrows():
        iata2 = row2['IATA']
        color, marker, linewidth = (1, 0, 0, 0.7), 'x', 1  # for cancelled flights line is red and marked as 'X'
        if iata == iata2:  # if flight is currently available then the line is green and etc.
            color, marker, linewidth = (0.4, 0.8, 0), 'o', 2
            break

    plt.plot([long, tall_lon], [lat, tall_lat],
             color=color, linewidth=linewidth, marker=marker,
             transform=ccrs.PlateCarree())
    plt.text(long + 0.9, lat - 1, iata,
             horizontalalignment='right',
             transform=ccrs.PlateCarree())

plt.savefig('flights.png')
plt.show()
