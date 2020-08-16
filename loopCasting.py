week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(',')
avg_temp = 0
total = 0
for temp in week_temps_f:
    total += float(temp)
avg_temp = total/(len(week_temps_f))
