name = "sdtete1223!!!023"
#name = "sdtete1223023"
#檢查是不是字串單純只有字母跟數字的神器
print(name.isalnum())

song = """When an eel grabs your arm,
    And it causes great harm,
    That's a - a moray!"""

arg = ('roast beef', 'fish') 

print('''My kitty cat likes %s,
My kitty cat likes %s''' % arg)


print(song.replace(' m', ' M'))



print('''Dear {salutation} {name},
we are sorry that our {product}
is in your room'''.format(salutation = 'Ambassador', name = 'Steven', product = 'shampoo')
)
