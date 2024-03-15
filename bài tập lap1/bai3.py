tienbandau=10000
amount_after_5_years=tienbandau*(6/100)*5
amount_after_10_years=tienbandau*(6/100)*10
growth_rate=(amount_after_10_years-amount_after_5_years)/amount_after_5_years
print('số tiền sau 5 năm là {}\n ,số tiền sau 10 năm là {}\n, tỉ lệ tăng trưởng của số tiền có sau 10 năm so với 5 năm là {}'.format(amount_after_5_years,amount_after_10_years,growth_rate))