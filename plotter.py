import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import sys
import os

script_dir = os.path.dirname(__file__)  # 스크립트가 있는 폴더
file_path = os.path.join(script_dir, 'tldata.txt')

colors = ['#000000', '#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff']


def main():
    sys.stdin = open(file_path, 'r', encoding='utf-8')

    dealer = int(input("딜러 수: "))
    supporter = int(input("서포터 수: "))

    idx = 0
    tl = [[] for _ in range(dealer + supporter)]
    char_names = []

    font_path = "C:/Windows/Fonts/malgun.ttf"
    font_prop = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_prop)
    fig, ax = plt.subplots()

    # total_time = int(input("총 시간(분): ")) * 60
    for i in range(dealer):
        name = input(f"딜러 {i+1} 이름: ")
        char_names.append(name)
        delays = []

        while(True):
            dtime = float(input(f"{name} 딜레이: "))
            if(dtime <= 0):
                break
            delays.append(dtime)
        
        while(True):
            try:
                time = time_parser(input(f"{name} 시간: "))
                if(time <= 0):
                    break
            except:
                break
            tl[idx].append(time)
        
        plt.plot(tl[idx], [idx / 10 for _ in range(len(tl[idx]))], marker='v', color=colors[idx], markersize=5, linewidth=1.5)

        for delay in delays:
            shifted = [x - delay for x in tl[idx]]
            plt.plot(shifted, [idx / 10 for _ in range(len(tl[idx]))], marker='o', color=colors[idx], markersize=5, linewidth=1.5)
            for t in shifted:
                plt.axvline(x=t, color=colors[idx], linewidth=1, alpha=0.5)
        idx += 1

    for i in range(supporter):
        name = input(f"서포터 {i+1} 이름: ")
        char_names.append(name)

        delay = float(input(f"{name} 딜레이: "))
        buff_time = float(input(f"{name} 지속 시간: "))

        while(True):
            try:
                time = time_parser(input(f"{name} 시간: "))
                if(time <= 0):
                    break
            except:
                break
            tl[idx].append(time)

        plt.plot(tl[idx], [idx / 10 for _ in range(len(tl[idx]))], marker='v', color=colors[idx], markersize=5, linewidth=1.5)
        
        delay_shifted = [x - delay for x in tl[idx]]
        plt.plot(delay_shifted, [idx / 10 for _ in range(len(tl[idx]))], marker='o', color=colors[idx], markersize=5, linewidth=1.5)
        
        buff_shifted = [x - delay - buff_time for x in tl[idx]]
        plt.plot(buff_shifted, [idx / 10 for _ in range(len(tl[idx]))], marker='x', color=colors[idx], markersize=5, linewidth=1.5)
        
        for j in range(len(tl[idx])):
            # plt.axvspan(delay_shifted[j], buff_shifted[j], ymin=(idx / 10 - 0.1), ymax=(idx / 10), color = colors[idx], alpha=0.3)
            rect = patches.Rectangle((delay_shifted[j], (idx / 10 - 0.1)), buff_shifted[j] - delay_shifted[j], 0.1, facecolor = colors[idx], alpha=0.3)
            ax.add_patch(rect)
        idx += 1

    plt.gca().invert_xaxis()
    plt.gca().xaxis.set_major_formatter(FuncFormatter(time_formatter))
    plt.xticks(rotation=-90)
    plt.yticks([x / 10 for x in range(len(char_names))], char_names)
    plt.subplots_adjust(bottom=0.2)
    plt.ylim(0, 1)

    for i, name in enumerate(char_names):
        plt.plot([], [], color=colors[i], label=name)  # 빈 plot 으로 범례 제작

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
