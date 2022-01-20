#Start of game
answer = input(
    "You and your best friend go camping in the woods. She offers to find wood to start the fire by herself so you could work on setting up the tent. Do you \nA-Tell her we should stay together at all times. \nor \nB- Agree to her offer and start working on the tent.")


#If you choose to stay together
if answer == "A":
  answer = input(
    "You and your friend stay together through the night but when you woke up you noticed she was not there. Do you \nA- Go look for her \nor \nB- Pack up the tent and leave since she probably got a headstart and is on her way home already")

#If you choose to look for her
  if answer == "A":
    answer = input(
      "Do you \nA- Look North \nor \nB- Look South")

#if you choose to look North
    if answer == "A":
      answer = input(
        "No Trail of her here. Do you \nA- Look South \nor \nB- Stop looking and head home")
#If you choose to look south second time
      if answer == "A":
        answer = input(
          "You found her petting a bear cub. You and her go back, pack up and head home. \nThe End.")
          #End1
#If you choose to stop looking for her
      elif answer == "B":
        answer = input(
          "You head home. You never found out what happened to your friend. The End.(Bad Ending)")
          #End2

#If you choose to look south
    elif answer == "B":
      answer = input(
        "you found her trying to get her bag back from a sneaky fox. You tell her just to forget about it and head home together. \nThe End.")
        #End3

#if you choose not to look for her
  elif answer == "B":
    answer = input(
      "She was not home. She was never found \nThe End.(Bad Ending)")
      #End4


#If you choose to seperate
elif answer == "B":
  answer = input(
    "You finish the tent and you see her on her way back with a ton of wood. \nYou both hear footsteps in the nearby bushes. Do you \nA- Investigate the bushes \nor \nB- Run and hide in the tent")
#if you choose to investigate the bushes
  if answer == "A":
    answer = input(
      "You see a baby wolf with huge paws. You and your friend laugh it off and pet the wolf. The next morning you two head home safely. \nThe End.")
      #End5

  elif answer == "B":
    answer = input(
      "You guys fell asleep. When you woke up you saw that there were GIANT footprints right outside the tent opening. You and your friend leave everything and rush home. Constantly living in fear of what was out there that night. \n The End.")
      #End6