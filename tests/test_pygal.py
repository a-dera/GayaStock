import pygal

p = pygal.Pie()
p.title = 'Browser usage'
p.add('IE', 20)
p.add('Firefox', 50)
p.add('Chrome', 30)

file = p.render()
file=str(file)

f= open('pie.html','w')
f.write(file)
f.close()