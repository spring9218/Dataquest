#Guided Project: Explore U.S. Births


f = open("US_births_1994-2003_CDC_NCHS.csv",'r').read()
data = f.split("\n")
####f = open("US_births_1994-2003_CDC_NCHS.csv",'r').read().split("\n")
print(data[0:10])



def read_csv(file):
    f = open(file,'r').read()
    data = f.split("\n")
    string_list = data[1:len(data)]
####string_list = open(file,'r').read().split("\n")[1:]
    final_list = []
    for line in string_list:
        int_fields = []
        string_fields = line.split(",")
        for item in string_fields:
            int_fields.append(int(item))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[0:10])



def month_births(data):
    births_per_month = {}
    for line in data:
        month = line[1]
        births = line[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_month_births = month_births(cdc_list)
print(cdc_month_births)
                


def dow_births(data):
    day_of_week = {}
    for line in data:
        day = line[3]
        births = line[4]
        if day in day_of_week:
            day_of_week[day] += births
        else:
            day_of_week[day] = births
    return day_of_week

cdc_day_births = dow_births(cdc_list)
print(cdc_day_births)



def calc_counts(data, column):
    counts = {}
    index = {'year':0, 'month':1, "dom":2, "dow":3}
    column_index = index[column]
    for line in data:
        column = line[column_index]
        births = line[4]
        if column in counts:
            counts[column] += births
        else:
            counts[column] = births
    return counts

cdc_year_births = calc_counts(cdc_list, 'year')
cdc_month_births = calc_counts(cdc_list, 'month')
cdc_dom_births = calc_counts(cdc_list, 'dom')
cdc_dow_births = calc_counts(cdc_list, 'dow')
print(cdc_year_births)
print(cdc_month_births)
print(cdc_dom_births)
print(cdc_dow_births)



