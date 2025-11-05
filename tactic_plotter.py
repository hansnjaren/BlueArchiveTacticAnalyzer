import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import math
import re
import os
import json

attacker_database = 'database/attacker.json'
supporter_database = 'database/supporter.json'
enemy_database = 'database/enemy.json'
script_dir = os.path.dirname(os.path.abspath(__file__))
timeline = os.path.join(script_dir, 'timeline.txt')

colors = ['#000000', '#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff']

with open(attacker_database, 'r', encoding='utf-8') as attacker_json:
    attacker_load = json.load(attacker_json)

attacker = {}
for item in attacker_load:
    key = item['name']
    value = item['delays']
    attacker[key] = value

with open(supporter_database, 'r', encoding='utf-8') as supporter_json:
    supporter_load = json.load(supporter_json)

supporter = {}
for item in supporter_load:
    key = item['name']
    value = {k: v for k, v in item.items() if k != 'name'}
    supporter[key] = value


with open(enemy_database, 'r', encoding='utf-8') as enemy_json:
    enemy_load = json.load(enemy_json)

enemy = []
for item in enemy_load:
    enemy.append(item)

def main():
    attacker_tl = {}
    supporter_tl = {}
    with open(timeline, 'r', encoding='utf-8') as f:
        text = f.read()
        pattern = r'\(?(\d{2}:\d{2}\.\d{3})\)?\s*C?([^\s>]+)(?:>([^\s]+))?'
        matches = re.findall(pattern, text)
        for time, char, target in matches:
            if (char in attacker):
                if((not target) or (target in enemy)):
                    attacker_tl.setdefault((char, target), []).append(time)
            if (char in supporter):
                if ((not target) or (target in attacker) or (target in enemy)):
                    supporter_tl.setdefault((char, target), []).append(time)

    char_names = []
    idx = 0
    tl = [[] for _ in range(len(attacker_tl) + len(supporter_tl))]
    init_time = 0

    font_path = "C:/Windows/Fonts/malgun.ttf"
    font_prop = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_prop)
    fig, ax = plt.subplots(figsize=(16, 4))

    for key, times in attacker_tl.items():
        (char, target) = key
        name = char
        if (target):
            name += f">{target}"
        char_names.append(name)
        delays = attacker[char]
        
        for time_text in times:
            tl[idx].append(time_parser(time_text))

        max_time = max(tl[idx])
        if (max_time > init_time):
            init_time = max_time

        plt.plot(tl[idx], [idx / 10 for _ in range(len(tl[idx]))], marker='v', color=colors[idx], markersize=5, linewidth=1.5)

        for delay in delays:
            shifted = [x - delay for x in tl[idx]]
            plt.plot(shifted, [idx / 10 for _ in range(len(tl[idx]))], marker='o', color=colors[idx], markersize=5, linewidth=1.5)
            for t in shifted:
                plt.axvline(x=t, color=colors[idx], linewidth=1, alpha=0.5)
        idx += 1

    supporter_UE2 = {}

    for (key, times) in supporter_tl.items():
        (char, target) = key
        name = char
        if (target):
            name += f">{target}"
        char_names.append(name)

        while (not supporter_UE2.get(char)):
            answer = input(f"UE rank 2 (전무 2성) required for {char}? [y/n] ")
            if answer in ['y', 'n', 'Y', 'N']:
                supporter_UE2[char] = answer.lower()
            else:
                print("\033[F\033[K\033[F")

        delay = supporter[char]['delay']
        buff_time = supporter[char]['duration']
        if (supporter_UE2[char]):
            buff_time *= 1.19

        for time_text in times:
            tl[idx].append(time_parser(time_text))

        max_time = max(tl[idx])
        if (max_time > init_time):
            init_time = max_time

        plt.plot(tl[idx], [idx / 10 for _ in range(len(tl[idx]))], marker='v', color=colors[idx], markersize=5, linewidth=1.5)
        
        delay_shifted = [x - delay for x in tl[idx]]
        plt.plot(delay_shifted, [idx / 10 for _ in range(len(tl[idx]))], marker='o', color=colors[idx], markersize=5, linewidth=1.5)
        
        buff_shifted = [x - delay - buff_time for x in tl[idx]]
        plt.plot(buff_shifted, [idx / 10 for _ in range(len(tl[idx]))], marker='x', color=colors[idx], markersize=5, linewidth=1.5)
        
        for j in range(len(tl[idx])):
            rect = patches.Rectangle((delay_shifted[j], (idx / 10 - 0.1)), buff_shifted[j] - delay_shifted[j], 0.1, facecolor = colors[idx], alpha=0.3)
            ax.add_patch(rect)
        idx += 1

    plt.gca().invert_xaxis()
    plt.gca().xaxis.set_major_formatter(FuncFormatter(time_formatter))
    plt.xticks([x * 30 for x in range(math.ceil(init_time / 30.0) + 1)], rotation=-90)
    plt.yticks([x / 10 for x in range(len(char_names))], char_names)
    plt.subplots_adjust(bottom=0.2)
    plt.ylim(0, 1)

    for i, name in enumerate(char_names):
        plt.plot([], [], color=colors[i], label=name)

    plt.tight_layout()
    plt.legend()

    plt.show()

def time_parser(time):
    min_sec, millisec = time.split('.')
    minute, second = min_sec.split(':')
    return int(minute) * 60 + int(second) + int(millisec) / 1000

def time_formatter(x, pos):
    m = int(x // 60)
    s = int(x % 60)
    ms = int((x - int(x)) * 1000)
    return f'{m:02d}:{s:02d}.{ms:03d}'

if __name__ == '__main__':
    main()
