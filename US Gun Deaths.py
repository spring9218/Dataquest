#Guided Project: US Gun Deaths


import csv
data = list(csv.reader(open("guns.csv", 'r')))
print(data[:5])

headers = data[0]
data = data[1:]
print(headers)
print(data[:5])

year_counts = {}
for line in data:
    year = line[1]
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print(year_counts)

import datetime
dates = [(datetime.datetime(int(line[1]), int(line[2]), 1)) for line in data]
print(dates[:5])

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)

sex_counts = {}
for line in data:
    sex = line[5]
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
print(sex_counts)

race_counts = {}
for line in data:
    race = line[7]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
print(race_counts)

census = list(csv.reader(open("census.csv", 'r')))
print(census)

race_census = {}
race_census['Native American/Native Alaskan'] = int(census[1][13])
race_census['Asian/Pacific Islander'] = int(census[1][14]) + int(census[1][15])
race_census['Hispanic'] = int(census[1][11])
race_census['White'] = int(census[1][10])
race_census['Black'] = int(census[1][12])
print(race_census)
print(race_counts)
race_per_hundredk = {}
for item in race_counts:
    race_per_hundredk[item] = race_counts[item] / race_census[item] * 100000
print(race_per_hundredk)

intents = [line[3] for line in data]
races = [line[7] for line in data]
homicide_race_per_hundredk = {}
for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in homicide_race_per_hundredk:
            homicide_race_per_hundredk[race] += 1
        else:
            homicide_race_per_hundredk[race] = 1
for item in race_census:
    homicide_race_per_hundredk[item] = homicide_race_per_hundredk[item] / race_census[item] * 100000
print(homicide_race_per_hundredk)


#Another way to code. May be more efficient.
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk

