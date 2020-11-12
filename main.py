név = input('Hogy hívnak? ')
nemed = input('Nő vagy férfi vagy? (n/f) ')
if nemed == 'n':
    előtag = 'Ms.'
elif nemed == 'f':
    előtag = 'Mr.' 
napszak = input('Milyen napszak van most? (r/du/e/é) ')
# r = reggel, du = délután, e = este, é = éjjel
if napszak == 'r':
  napszak = 'morning'
elif napszak == 'du':
  napszak = 'afternoon'
elif napszak == 'e':
  napszak = 'evening'
elif napszak == 'é':
  napszak = 'night'
print('Good ', napszak, ', ', előtag, ' ', név, '!', sep='')