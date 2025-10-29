# Blue Archive Tactic Analyzer (BATA)
BATA has 2 components right now: (1) Tactic timeline plotter and (2) Damage calculator. 

## Tactic timeline plotter
This will plot the attacker's attacking time and buffs duration with pyplot. 
You should know delay, the time when character uses their skill, and its duration. 

## Damage calculator
This will calculate average damage that will be dealt by dealer, and calculate success rate (dealing more than target) with Monte Carlo method. 
You should know critical rate, critical multiplier, stability, non-crit max damage, and number of attack of attackers. 
It is also possible to calculate average damage for attackers that has damage multiplier related to enemy's HP, but it may not be accurate since it is approximated to average damage. 