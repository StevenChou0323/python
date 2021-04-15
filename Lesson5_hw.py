things = ['mozzarella', 'cinderella', 'salmonella']

things.remove('salmonella')

surprise = ['Groucho', 'Chico', 'Harpo']

surprise[-1] = surprise[-1].lower()[::-1].capitalize()

even = [number for number in range(10) if number % 2 == 0]

start1 = ['fee', 'fie', 'foe']

rhymes = [('flop', 'got a mop'),('fope', 'turn the rope'),('fa', 'get ur ma')]

start2 = 'Someone better'

combine1 =" ".join([string.capitalize() + "! " for string in start1])

for first,second in rhymes:
    print(f"{combine1}{first.capitalize()}!")
    print(f"{start2} {second}")