class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        return self.targets

    def get_target_percents(self):
        return [(target / self.entry - 1) * 100 for target in self.targets]

    def get_target_banks(self):
        return [self.bank * target / self.entry for target in self.targets]

    def get_str_target(self, i):
        return f"{i + 1} target: {self.get_targets()[i]}\n" \
               f"Percent: {round(self.get_target_percents()[i], 3)}%\n" \
               f"Bank: {round(self.get_target_banks()[i], 3)}"

    def __str__(self):
        targets = "\n\n".join([self.get_str_target(i) for i in range(len(self.targets))])
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"


def read_data(file_name):
    with open(file_name) as file:
        return file.read()


def get_deals(raw_data):
    raw_deals = raw_data.split("-----")
    deals = []
    for raw_deal in raw_deals:
        bank_index = raw_deal.find('BANK:')
        entry_index = raw_deal.find('Вход:')
        target_index = raw_deal.find('Таргет:')
        out_index = raw_deal.find('Выход:')
        
        if bank_index == -1 or entry_index == -1 or target_index == -1 or out_index == -1:
            continue

        bank_str = raw_deal[bank_index + 5:entry_index]
        entry_str = raw_deal[entry_index + 5:target_index]
        target_str = raw_deal[target_index + 7:out_index]
        out_str = raw_deal[out_index + 6:]

        bank_num = int(bank_str)
        entry_num = float(entry_str)
        targets_num = [float(t) for t in target_str.split(";")]
        out_num = float(out_str)

        deals.append(StrategyDeal(bank_num, entry_num, targets_num, out_num))

    return deals


def write_data(file_name, data):
    f = open(file_name, 'w')
    f.write("\n\n-----\n\n".join([str(d) for d in data]))
    f.close()


def main():
    content = read_data('deals.txt')
    result = get_deals(content)
    write_data('out.txt', result)


if __name__ == '__main__':
    main() 
