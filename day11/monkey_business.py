#!/Users/mattray/miniconda3/bin python

import json
from copy import deepcopy

class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level




class Monkey:
    def __init__(self):
        self.items = None
        self.worry_change = None
        self.test = None
        self.if_true = None
        self.if_false = None
        self.inspections = 0
    
    def add_config(self, config):
        self.items = [Item(deepcopy(score)) for score in config["starting_items"]]
        self.test = lambda x: x % deepcopy(config['test']) == 0
        self.if_true = config["if_true"]
        self.if_false = config["if_false"]
        if config["op"][0] == '+':
            if config["op"][1] != 'old':
                self.worry_change = lambda x: x + deepcopy(config["op"][1]) 
            else:
                self.worry_change = lambda x: x + x
        elif config["op"][0] == '*':
            if config["op"][1] != 'old':
                self.worry_change = lambda x: x * deepcopy(config["op"][1]) 
            else:
                self.worry_change = lambda x: x * x

    def throw_items(self):
        for item in self.items:
            item.worry_level = self.worry_change(item.worry_level)
            item.worry_level = item.worry_level % 9699690
            result = self.test(item.worry_level)
            global all_monkeys
            if result:
                all_monkeys[self.if_true].items.append(item)
            else:
                all_monkeys[self.if_false].items.append(item)
            self.inspections += 1
        self.items = []

    
def part1():
    with open('configs.json', 'r') as f:
        configs = json.load(f)
    global all_monkeys
    all_monkeys = []
    for config in configs['monkeys']:
        new_monkey = Monkey()
        new_monkey.add_config(config)
        all_monkeys.append(new_monkey)
    
    for _ in range(20):
        for monkey in all_monkeys:
            monkey.throw_items()


    activity = [monkey.inspections for monkey in all_monkeys]
    print(activity)
    max_activity = sorted(activity)
    print(max_activity)
    print(max_activity[-2] * max_activity[-1])


def part2():
    with open('configs.json', 'r') as f:
        configs = json.load(f)
    global all_monkeys
    all_monkeys = []
    for config in configs['monkeys']:
        new_monkey = Monkey()
        new_monkey.add_config(config)
        all_monkeys.append(new_monkey)
    madeit = True
    for i in range(10000):
        for monkey in all_monkeys:
            monkey.throw_items()
        
    
    activity = [monkey.inspections for monkey in all_monkeys]
    print(activity)
    max_activity = sorted(activity)
    print(max_activity)
    print(max_activity[-2] * max_activity[-1])
    


if __name__ == '__main__':
    #part1()
    part2()