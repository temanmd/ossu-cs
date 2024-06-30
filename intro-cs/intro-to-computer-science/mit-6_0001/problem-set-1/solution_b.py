def calc_number_of_months(annual_salary, portion_saved, total_cost, semi_annual_raise):
    portion_down_payment = 0.25
    current_savings = 0
    investment_annual_return = 0.04
    monthly_salary = annual_salary / 12
    down_payment = total_cost * portion_down_payment
    number_of_months = 0
    monthly_salary_portion_saved = monthly_salary * portion_saved

    while current_savings < down_payment:
        additional_monthly_return = current_savings * investment_annual_return / 12
        current_savings += monthly_salary_portion_saved
        current_savings += additional_monthly_return
        number_of_months += 1
        if number_of_months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
            monthly_salary_portion_saved = monthly_salary * portion_saved

    return number_of_months


def main():
    annual_salary = int(input("Enter your annual salary: ").strip())
    portion_saved = float(
        input("Enter the percent of your salary to save, as a decimal: ").strip()
    )
    total_cost = int(input("Enter the cost of your dream home: ").strip())
    semi_annual_raise = float(
        input("Enter the semi­annual raise, as a decimal: ").strip()
    )

    result = calc_number_of_months(
        annual_salary, portion_saved, total_cost, semi_annual_raise
    )
    print(f"Number of months: {result}")


if __name__ == "__main__":
    main()
