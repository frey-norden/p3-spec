medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
mc = sorted(medals.items(), key=lambda x:x[1], reverse=True)
top = []
for x in range(3):
    top.append(mc[x])

print(top)

top_performers = dict(top)
tp = list(top_performers.keys())
top_three = []
for i in range(3):
    top_three.append(tp[i])

print(top_three)
