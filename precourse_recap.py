number_of_bones=int(input("On average, how many bones does an adult human have in their body: "))
if number_of_bones >= 190 and number_of_bones <= 205:
  print("You are bone's throw away. Why don't you give it another go?")
if number_of_bones > 206 and number_of_bones < 213:
  print("Snap! You've cracked it!(hopefully just methaporically) On average, adult human beings are believed to have between 206 and 213 bones in their bodies.")
if number_of_bones > 214 and number_of_bones < 225:
  print("You are bone's throw away. Why don't you give it another go?")
if number_of_bones >= 300:
  print("I wonder how many of them are funny.")
if number_of_bones < 100:
  print('How humerus. Try again.')
else :
  print("This won't crack it.")
