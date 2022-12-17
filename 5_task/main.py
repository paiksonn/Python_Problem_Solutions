import json
from random import randint


class WorkHours:

    def work_hours(self, month, year):
        return randint(20, 23)

class Income_Per_Hour:

    def income_per_hour(salary, month, year):
        hour_income = salary/WorkHours().work_hours(month,year)
        return round(hour_income, 2)


def main():

    with open('input.json', 'r') as inputt:
        data = json.load(inputt)
        salary, month, year = data.get("salary"), data.get('month'), data.get('year')
        PerHourSalary = Income_Per_Hour.income_per_hour(salary, month, year)

    with open('output.json', 'w') as outputt:
        data["hour_income"] = perHourSalary
        outputt.write(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    main()
