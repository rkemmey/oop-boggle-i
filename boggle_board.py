import string
import random
import re

class BoggleBoard:
  
  def __init__(self):
    print('____\n____\n____\n____')

  # step 1
  # def shake(self):
  #   letters = string.ascii_uppercase
  #   bog_str = ""
  #   for i in range(16):
  #     random_number = random.randint(0, 25)
  #     bog_str += letters[random_number]
  #   print(f'{bog_str[0:4]}\n{bog_str[4:8]}\n{bog_str[8:12]}\n{bog_str[12:]}')
  #   print(f'\n{bog_str}')

  # step 2
  def shake(self):
    bog_str = ""
    bog_dice = [['AAEEGN'], ['ELRTTY'], ['AOOTTW'], ['ABBJOO'],
                ['EHRTVW'], ['CIMOTU'], ['DISTTY'], ['EIOSST'], 
                ['DELRVY'], ['ACHOPS'], ['HIMNQU'], ['EEINSU'],
                ['EEGHNW'], ['AFFKPS'], ['HLNNRZ'], ['DEILRX']]
    random_order = random.sample(range(0,16), 16)
    for r in random_order:
      for b in bog_dice[r]:
        random_number = random.randint(0, 5)
        bog_str += b[random_number]
    if "Q" in bog_str:
      bog_str = bog_str.replace('Q', 'Qu')
      #spaced_text = " ".join(bog_str)
    spaced_str = ''
    #count = 0
    for (i, x) in enumerate(bog_str):
      #print(i)
      if not 'Q' in x:
        spaced_str = spaced_str + x + ' '
        #count +=1
      else:
        spaced_str += x
    print(spaced_str)
    #formatted_text = re.sub(r' {1}', '\n', spaced_str)
    #print(formatted_text)
    print(f'{bog_str[0:4]}\n{bog_str[4:8]}\n{bog_str[8:12]}\n{bog_str[12:]}')

game = BoggleBoard()
game.shake()
