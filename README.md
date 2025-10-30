# Blue Archive Tactic Analyzer (BATA)
BATA has 3 components right now: (1) Tactic timeline plotter and (2) Damage calculator, (3) Tactic parser. 

## Tactic timeline plotter
This will plot the attacker's attacking time and buffs duration with pyplot. 
You should know delay, the time when character uses their skill, and its duration. 

## Damage calculator
This will calculate average damage that will be dealt by dealer, and calculate success rate (dealing more than target) with Monte Carlo method. 
You should know critical rate, critical multiplier, stability, non-crit max damage, and number of attack of attackers. 
It is also possible to calculate average damage for attackers that has damage multiplier proportional to enemy's HP (either remaining HP or damage taken), but it may not be accurate since it is approximated to average damage. 

## Tactic parser
This will parse tactic that fits to Tactic timeline plotter, listing characters and skill using time. The output will be written in output.txt. Skill using time should appear earlier than character. The format should be like this: 
> time character > target
Additional description in front of or back of the format does not care, but there should be no additional text inside the format, except closing parenthesis `)`. 
This format is okay: 
``` 
페이즈 전환 직후 (01:31.966) 돌마리 - 9코 (영상 8.6코 01:30.866) 돌쿠라코 - (01:29.966) 사츠키 `8/12` `6640만`
7코 (영상 9.9코 01:20.633) 수로코>게부라 - (01:19.466) 돌마리 `과부하 OFF 후 ON`
```
Set `find_target` to get skills only targeted to boss. 