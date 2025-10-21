# take data from here: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
import pandas as pd

data = pd.read_csv("squirrel_data_NYC_2018.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(f"Gray: {gray_squirrels_count}\nCinnamon: {red_squirrels_count}\nBlack: {black_squirrels_count}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)
