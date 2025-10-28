import random
from dataclasses import dataclass
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math
import sys
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'dealdata.txt')

@dataclass
class Attack:
    crit_rate: float = 0.0
    crit_mult: float = 1.0
    max_deal: int = 0
    stab: float = 1.0
    repeat: int = 0

def main():
    sys.stdin = open(file_path, 'r', encoding='utf-8')
    deal_tl = []
    data_list = []
    cnt = 0
    avg_sum = 0

    font_path = "C:/Windows/Fonts/malgun.ttf"
    font_prop = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_prop)

    num_data = int(input("Data number: "))
    target = int(input("Target damage: "))
    interval = int(input("Histogram interval: "))

    while(True):
        crit_rate = float(input("Critical rate(%)(put negative number to stop): "))
        if(crit_rate < 0):
            break
        crit_mult = float(input("Critical multiplier(%): "))
        stab = float(input("Stability(%): "))
        max_deal = int(input("Non-crit max damage: "))
        repeat = int(input("Number of attacks: "))
        deal_tl.append(Attack(crit_rate / 100, crit_mult / 100, max_deal, stab / 100, repeat))
    
    print("Data collection finished")

    for j in range(num_data):
        total_deal = 0
        for i in range(len(deal_tl)):
            total_deal += crit_simul(deal_tl[i])
        if(total_deal >= target):
            cnt += 1
        data_list.append(total_deal)
    
    print("Simulation done")

    for i in range(len(deal_tl)):
        avg_sum += avg_deal(deal_tl[i])

    max_val = math.ceil(max(data_list) / interval) * interval
    min_val = math.floor(min(data_list) / interval) * interval
    bins = list(range(min_val, max_val + interval, interval))
    counts, bins, patches = plt.hist(data_list, bins=bins)
    
    for patch, left_edge in zip(patches, bins[:-1]):
        if(left_edge >= target):
            patch.set_facecolor('red')
        else:
            patch.set_facecolor('blue')
    
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    plt.xlabel(f"Success rate: {cnt / num_data * 100:.2f} %, Average damage: {avg_sum}")
    plt.axvline(x=target, color='black', linewidth=1)
    plt.show()


def crit_simul(attack: Attack):
    sum = 0
    for _ in range(attack.repeat):
        is_crit = random.random() < attack.crit_rate
        stab_result = random.uniform(attack.stab, 1)
        sum += int(attack.max_deal * stab_result * (attack.crit_mult if is_crit else 1.0))
    return sum

def avg_deal(attack: Attack):
    return int(attack.repeat * attack.max_deal * (1 + attack.stab) / 2.0 * (1 + attack.crit_rate * (attack.crit_mult - 1)))

if(__name__ == '__main__'):
    main()
