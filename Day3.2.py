def solve(meal_cost, tip_percent, tax_percent):
    tip=meal_cost*0.01*tip_percent
    tax=meal_cost*0.01*tax_percent
    print(round(meal_cost+tip+tax))
    


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
