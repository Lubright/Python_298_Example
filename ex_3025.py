season_map = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
              6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn',
              11: 'Autumn', 12: 'Winter'}

n = eval(input())

if n in season_map:
    print(season_map.get(n))
else:
    print('Month doesn\'t exist!')
