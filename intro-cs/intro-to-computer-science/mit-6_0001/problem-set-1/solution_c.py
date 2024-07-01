def calc_savings_for_rate(rate, annual_salary):
    months_to_achieve = 36
    semi_annual_raise = 0.07
    investment_annual_return = 0.04
    current_savings = 0
    monthly_salary = annual_salary / 12
    monthly_salary_portion_saved = monthly_salary * rate

    for i in range(months_to_achieve):
        additional_monthly_return = current_savings * investment_annual_return / 12
        current_savings += monthly_salary_portion_saved
        current_savings += additional_monthly_return
        if (i + 1) % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
            monthly_salary_portion_saved = monthly_salary * rate

    return current_savings


def calc_best_savings_rate(annual_salary):
    portion_down_payment = 0.25
    total_cost = 1_000_000
    down_payment = total_cost * portion_down_payment
    low_rate = 0
    high_rate = 10000
    guess_savings = 0
    steps = 0

    while low_rate <= high_rate:
        steps += 1
        guess = (low_rate + high_rate) // 2
        rate = guess / 10000
        guess_savings = calc_savings_for_rate(rate, annual_salary)
        if abs(guess_savings - down_payment) <= 100:
            return [True, rate, steps]
        if guess_savings > down_payment:
            high_rate = guess - 1
        else:
            low_rate = guess + 1

    return [False, None, None]


def main():
    annual_salary = int(input("Enter your annual salary: ").strip())

    result, best_savings_rate, steps = calc_best_savings_rate(annual_salary)

    if result:
        print(f"Best savings rate: {best_savings_rate}")
        print(f"Steps in bisection search: {steps}")
    else:
        print("It is not possible to pay the down payment in three years.")


if __name__ == "__main__":
    main()
