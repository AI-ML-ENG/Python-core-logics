import statistics as s
value=[12,34,56,67,89,90,9,87,65,43,21,48]
highest_value=max(value)
mean=s.fmean(value)
value1=[10,10,10,10,10]
standard_dev=s.stdev(value1)
median=s.median(value)
hours=[1,2,3,4,5]
value1=[10,25,30,55,50]
variance=s.variance(value1)
regression=s.linear_regression(hours,value1)
tomorrow_sales=(regression.slope*6)+regression.intercept
core=s.correlation(hours,value1)
print(core)
quant=s.quantiles(hours,n=4)
print(quant)


