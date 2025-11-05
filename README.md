# Blue Archive Tactic Analyzer (BATA)
BATA has 2 components right now: (1) Tactic timeline plotter and (2) Damage calculator

## Tactic timeline plotter
This will plot the attacker's attacking time and buffs duration based on timeline. If the character data is NOT in database JSON file, it does not work properly. If you have any data that are not in database, feel free to make PR. 

All buff/debuff durations of supporters are written in basic duration. So you must answer if the supporters are higher than unique equipment (UE) rank 2, and their buff/debuff duration changes when they reach UE rank 2. For convenience, it assumes that passive skill (PS) level is 10 (MAX) if UE rank 2 is required. 

This feature has combined the legacy plotter (whith works with data that users should give delays and times for input) and tactic parser. Both are in `deprecated` directory. 

To use it properly, you should write your timeline in this format:

> time character > target

Additional description in front of or back of the format does not care, but there should be no additional text inside the format, except closing parenthesis `)`. 

This is the example of proper timeline format: 

``` 
페이즈 전환 직후 (01:31.966) 돌마리 - 9코 (영상 8.6코 01:30.866) 돌쿠라코 - (01:29.966) 사츠키 `8/12` `6640만`
7코 (영상 9.9코 01:20.633) 수로코>게부라 - (01:19.466) 돌마리 `과부하 OFF 후 ON`
```

## Damage calculator
This will calculate average damage that will be dealt by dealer, and calculate success rate (dealing more than target) with Monte Carlo method. 
You should know critical rate, critical multiplier, stability, non-crit max damage, and number of attack of attackers. 

It is also possible to calculate average damage for attackers that has damage multiplier proportional to enemy's HP (either remaining HP or damage taken), but it may not be accurate since it is approximated to average damage. 
