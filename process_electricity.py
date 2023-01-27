import os
import json
import sys

last_line=""
footprintdict={}

with open("latest_electricity.csv") as f:
        for line in f:
                pass
        last_line = line

with open("carbonfootprint.json") as f:
        footprintdict = json.load(f)

last_line = last_line.split(",")
last_line = last_line[3:]
last_line[47] = last_line[47].replace("\n", "")

kwh_vals_day = [float(x) for x in last_line]
price_vals_day = [round(float(x) * 0.2081, 6) for x in last_line]
carbon_day = [round(float(footprintdict["data"]["carbonIntensity"]) * x, 4) for x in kwh_vals_day]

if sys.argv[1] == "kwh":
        total = 0.0
        for val in kwh_vals_day:
                total += val
        print(round(total, 2))
elif sys.argv[1] == "price":
        total = 0.0
        for val in price_vals_day:
                total += val
        print(round(total, 2))
elif sys.argv[1] == "carbon":
        total = 0.0
        for val in carbon_day:
                total+=val
        print(round(total / 1000, 2))