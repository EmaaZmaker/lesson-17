def tip_calc(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print("the total amount is",total)
tip_calc(5,7)