text = ''' It should be clear for everyone that you have no business on campuses unless you’re fit and healthy. Even a runny nose should be treated with the seriousness required by the situation.

Please follow the instructions below before coming to campuses:

    No less than seven days after you have been infected with a respiratory infection or suspected of COVID-19 infection and you have had no symptoms during the last three days.
     
    14 days after you (or a person living in the same household) have been ill due to diagnosed coronavirus disease and you (or the other person) have had no symptoms during the last three days.
     
    You have not been in the same space with a person diagnosed with coronavirus disease during the last 14 days.
  '''
lines = text.splitlines()
print(len(lines))
print(lines[2])
line2 = lines[2]
werds = line2.split()
print(werds)

print('Now, we glue it back together with join() method')
glue = ('/')
gluedup = glue.join(werds)
print(gluedup)



