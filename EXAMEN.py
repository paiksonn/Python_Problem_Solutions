

class StrategyDeal:
    def __init__(self, entry, targets, close, bank):
        self.entry = entry
        self.targets = [Target(bank, entry, target) for target in targets]
        self.close = close
        self.bank = bank
        
    def get_targets(self):
        return [target.get_out_price() for target in self.targets]

    def get_target_percents(self):
        [target.round((self.target/self.close - 1) * 100, 3) for target in self.targets]

    def get_target_banks(self):
        target.round(self.bank * target.round((self.target/self.close - 1) * 100, 3), 3)) for target in self.targets]

    def __str__(self):
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"
        


def read_data(file_name):
    f = open(file_name)
    data = f.readlines().strip()
    f.close()
    return data
    
def prepare_data(data):
    entry, close, bank = 0, 0, 0
    targets = []
    for line in data.split('\n'):
        if line.startswith('Вход: '):
            entry = line.replace('Вход: ', '')


def write_data(file_name, data):
    f = open(file_name, 'w')
    f.write(data)
    f.close()

def main():
    content = read_data('deals.txt')
    stratagy = StrategyDeal()
    result = 
    write_data('out.txt', result)
   
if __name__ == '__main__':    
    main() 
