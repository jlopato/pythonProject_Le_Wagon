le_wagon_team = [
{'name': 'ben', 'age': 31, 'country': 'france', 'hobbies': ['coding', 'biking']},
{'name': 'quinn', 'age': 26, 'country': 'ireland', 'hobbies': ['skiing']},
{'name': 'sasha', 'age': 24, 'country': 'lebanon', 'hobbies': ['sports']},
{'name': 'alex', 'age': 28, 'country': 'austria', 'hobbies': []} ]

print(le_wagon_team[0]['hobbies'][0])

print(le_wagon_team[1]['age'])
print(le_wagon_team[3]['age'])

print(le_wagon_team[1].get('age'))

le_wagon_team[0]['hobbies'].remove('biking')
print(le_wagon_team[0])

le_wagon_team[3]['hobbies'].append('skiing')
print(le_wagon_team[3])