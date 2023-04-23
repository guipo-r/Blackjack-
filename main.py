import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Dealing function
def deal_card(nr_cards):
  new_card = random.choices(cards, k = nr_cards)
  return new_card

def play():
  print(logo)
  
  on = True
  user = True
  dealer = True
  while on:
    #Cards drawn from deck
    dealer_hand = deal_card(2)
    user_hand = deal_card(2)
    
    #Determine initial scores
    dealer_score = sum(dealer_hand)
    user_score = sum(user_hand)
    
    #Reveal my hand
    print(f"Your cards: {user_hand}.|| Current score: {user_score}\n")
    
    #Reveal dealer's first card
    print(f"The dealer drew a {dealer_hand[0]} as first card\n")
    
    #Checking Blackjack in the first draw
    if dealer_score == 21:
      print("Dealer got Blacjack! You lose!")
      print(f"Dealer cards: {dealer_hand}")
      on = False
      user = False
      dealer = False
      break
    
    if user_score == 21:
      print(f"Your cards: {user_hand}.|| You got 21! Blackjack! You win!")
      print(f"Dealer cards: {dealer_hand}\n")
      on = False
      user = False
      dealer = False
      break
    
    #User's hand check
    while user:
      ask = input(f"Type 'y' to get another card, type 'n' to pass: ")
      if ask == 'y':
        user_hand = user_hand + deal_card(1)
        user_score = sum(user_hand)
        
        if user_score == 21:
          print(f"Your cards: {user_hand} || Blackjack! Let's see dealer's hand \n")
          user = False
          break
        elif user_score > 21:
          for i in range(len(user_hand)):
            if user_hand[i] == 11:
              user_hand[i] = 1
              user_score = sum(user_hand)
              print(f"Your cards: {user_hand} || Ace conversion! Current score: {user_score}")
          if user_score > 21:
            print(f"Your cards: {user_hand} || Current score: {user_score}")
            print("You lose!\n")
            user = False
            dealer = False
            on = False
            break
          elif user_score == 21:
            print(f"Your cards: {user_hand} || Blackjack! Let's see dealer's hand \n")
            user = False
            break
        else:
          print(f"Your cards: {user_hand} || Current score: {user_score}\n")
      
      elif ask == 'n':
        if user_score > 21:
          print("You lose!")
        user = False
      else:
        print(f"You entered an invalid option.")
    
    #Dealer's hand check
    while dealer:
      if dealer_score >= 17:
        print(f"Dealer got {dealer_hand}. Score: {dealer_score}")
        if dealer_score < 21 and dealer_score > user_score:
          print(f"Dealer got {dealer_score} and you got {user_score}. You lose!")
          on = False
          dealer = False
          break
        elif dealer_score < 21 and dealer_score < user_score and user_score < 21:
          print(f"Dealer got {dealer_score} and you got {user_score}. YOU WIN! :) ")
          on = False
          dealer = False
          break
        elif dealer_score < 21 and dealer_score == user_score:
          print(f"Dealer got {dealer_score} and you got {user_score}. It's a DRAW!")
          on = False
          dealer = False
          break
        else:
          for i in range(len(dealer_hand)):
            if dealer_hand[i] == 11:
              dealer_hand[i] = 1
              dealer_score = sum(dealer_hand)
          print(f"Dealer cards: {dealer_hand}. Score: {dealer_score}")
          
      while dealer_score < 17:
        dealer_hand = dealer_hand + deal_card(1)
        dealer_score = sum(dealer_hand)
        if dealer_score == 21:
          print(f"Dealer got {dealer_hand}. Score: {dealer_score}")
          print(f"Blackjack! Dealer wins!\n You Lose!")
          on = False
          dealer = False
          break
        elif dealer_score > 21:
          for i in range(len(dealer_hand)):
            if dealer_hand[i] == 11:
              dealer_hand[i] = 1
              dealer_score = sum(dealer_hand)
          if dealer_score > 21:
            print(f"Dealer got {dealer_hand}. Score: {dealer_score}")
            print("You win! Congratulations!")
            on = False
            dealer = False
            break
          elif dealer_score == 21:
            print(f"Dealer got {dealer_hand}. Score: {dealer_score}")
            print(f"Blackjack! You lose!! \n")
            on = False
            dealer = False
            break
          elif dealer_score >= 17 and dealer_score < 21:
            if dealer_score > user_score:
              print(f"Dealer got {dealer_score} and you got {user_score}. You lose!")
            elif dealer_score < user_score:
              print(f"Dealer got {dealer_score} and you got {user_score}. YOU WIN! :) ")
            else:
              print(f"Dealer got {dealer_score} and you got {user_score}. It's a DRAW!")
            on = False
            dealer = False
            break
        else:
          print(f"Dealer got {dealer_hand}. Score: {dealer_score}")
          if dealer_score >= 17 and dealer_score < 21:
            if dealer_score > user_score:
              print(f"Dealer got {dealer_score} and you got {user_score}. You lose!")
              on = False
              dealer = False
              break
            elif dealer_score < user_score:
              print(f"Dealer got {dealer_score} and you got {user_score}. YOU WIN! :) ")
              on = False
              dealer = False
              break
            else:
              print(f"Dealer got {dealer_score} and you got {user_score}. It's a DRAW!")
              on = False
              dealer = False
              break
  
  game_restart = input(f"Do you want to play again? Type 'y' if you do, or 'n' if you pass:\n")
  if game_restart == 'y':
    clear()
    play()
  else:
    print(f"Thanks for playing! Come back soon!")

play()
  