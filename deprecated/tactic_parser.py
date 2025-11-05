import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
timeline = os.path.join(script_dir, '..', 'timeline.txt')
output = os.path.join(script_dir, 'output.txt')

def main():
    parsed_tl = {}
    find_target = ''
    with open(timeline, 'r', encoding='utf-8') as f:
        text = f.read()
        pattern = r'\(?(\d{2}:\d{2}\.\d{3})\)?\s*([^\s>]+)(?:>([^\s]+))?'
        matches = re.findall(pattern, text)
        for time, char, target in matches:
            if(not target or target == find_target):
                parsed_tl.setdefault(char, []).append(time)

    with open(output, 'w', encoding='utf-8') as f:
        for char, time_list in parsed_tl.items():
            print(char, file=f)
            for time in time_list:
                print(time, file=f)


if __name__ == '__main__':
    main()
