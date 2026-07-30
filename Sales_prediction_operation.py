import statistics as s
import math as m
years=[1,2,3,4,5,6]
sales_revenue=[50,55,62,68,75,81]
current_prices=[12.50,15.99,22.00,145.00,18.50,29.99,110.00,25.00]
next_year_sales_prediction=s.linear_regression(years,sales_revenue)
print(next_year_sales_prediction)
next_year_sales=(next_year_sales_prediction.slope*7)+next_year_sales_prediction.intercept
print(next_year_sales)
premium_product=s.quantiles(current_prices,n=4)
for i in current_prices:
    if i >= 75.0:
        print("premium products price",i)
stability=s.stdev(current_prices)
print(stability)
for i in current_prices:
    new_list=m.ceil(i)
    print(new_list)


