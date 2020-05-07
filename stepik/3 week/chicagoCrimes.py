import csv
import datetime as dt

with open("Crimes.csv") as c:
    reader = csv.reader(c)
    headers = next(reader)
    crime_type_idx = headers.index('Primary Type')
    crime_date_idx = headers.index('Date')
    m2015 = []
    for row in reader:
        crime_year = dt.datetime.strptime(row[crime_date_idx],
                                          '%m/%d/%Y %I:%M:%S %p').year
        if crime_year == 2015:
            crime_type = row[crime_type_idx]
            m2015.append(crime_type)
    print(max(m2015, key=m2015.count))
