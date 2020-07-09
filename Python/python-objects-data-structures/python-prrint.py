print('This is a {} string'.format('Inserted'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777
print('The result was {r}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))

# f-string and this new to python 3.6
name = 'iskander'
print(f'Hello, his name is {name}')
