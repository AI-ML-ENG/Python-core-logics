import statistics as s
import math as m
import datetime as dt
trip=dt.datetime(2026,7,8,11,2)
trip_duration=trip-dt.datetime(2026,7,8,10,5)
print("the time for this trip is",trip_duration)
delivery_times=[42,38,51,47,45]
mean=s.fmean(delivery_times)
print("The avg is ",mean)
meadian=s.median(delivery_times)
print("the consistency in delivery is",meadian)
for_knowing_avg=s.stdev(delivery_times)
print("The the consistent rate per delivery is",for_knowing_avg)
distance_travelled=12.7
paid_amount_on=m.ceil(distance_travelled)
print("The paid amount on this trip is ",paid_amount_on)


