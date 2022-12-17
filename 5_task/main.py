import json
from random import randint

class SomeNumber:
    def __init__(self, month, year):
        self.month = month
        self.year = year


    def get_number(self):
        return randint(20, 23)


class CalculateHourSalary:
    def __init__(self, input_name_file='input.json', output_name_file='output.json'):
        self.input_name_file = input_name_file
        self.output_name_file = output_name_file

    def get_hour_income(self):
        with open(self.input_name_file, "r") as input_file:
            data = json.load(input_file)
            days_in_month = SomeNumber(data['month']), data['year'].get_number()
            data['hour_income'] = round(data['salary'] / (days_in_month * 8), 2)
        return data

    def write(self, data_json):
        with open(self.output_name_file, 'a+') as result:
            json.dump(data_json, result)
