rolls = [1, 2, 3, 4, 5, 6]

def add_roll(rolls, roll):
   new_rolls = rolls.copy()
   new_rolls.append(roll)
   return new_rolls

print(add_roll(rolls, 7))
print(rolls)
