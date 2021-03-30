letter = 'o'

if letter == 'a' or letter == 'e' or letter == 'i' or \
    letter == 'o' or letter == 'u':
    print("是母音")
else:
    print("子音")

vowels = 'aeiou'
print(letter in vowels)

a = 280
b = "blah" * 50
if diff:= a - len(b) >= 0:
    print("test1")
else:
    print("test2")



secret = 5
guess = 5
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("right")


small = True
green = False

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")


#使用and not來寫判斷,不過少用not當判斷(不夠直觀)
if small and not green:
    print("cherry")

#使用海象運算子
if compare:= small and not green:
    print("cherry")