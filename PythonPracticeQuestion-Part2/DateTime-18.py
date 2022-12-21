#Python Program to Count date on a particular weekday in given range of Years
from datetime import date
dt = 13
weekdy = 5
start_yr = 1950
end_yr = 2020

start_dt = date(start_yr, 1, dt)
end_dt = date(end_yr, 1, dt)