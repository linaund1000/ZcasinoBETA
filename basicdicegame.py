'''
game is played between casino and player
'''
import random

from Users.player import Player
def randomdice():
    d = []
    d.append(random.randint(1,6))    
    d.append(random.randint(1,6))
    return sum(d)
def get_bet(player_money):
 
    bet = input('how much money you want to bet? : ')
    

    try :
        bet = int(bet)
        if bet < 1:
            return get_bet(player_money)
        if bet > player_money:
            print('bet less than your money, your amount of money is :', player_money)
            return get_bet(player_money)
        else:
            return bet
    except: 
        return get_bet(player_money)

def play_again_quest(player_money):
    if player_money < 1:
        print('you lost all your money')

        return False
    i = input('would you like to play again or not, please enter y or n :')
    while i.lower() not in ['y','n']:
        i = input('tell me what you want')
    if i.lower() == 'y':
        return True
    elif i.lower() == 'n':
        return False    
    
def dice_game_starter(player_money):
    
        player_bet = get_bet(player_money)

        player_dice = randomdice()
        casino_dice = randomdice()
        print('you threw his dices and sum of them is ',player_dice)
        print('casino threw his dices and sum of them is ',casino_dice)

        if casino_dice < player_dice:
            player_money += player_bet
            print(f'you won {player_bet}!!!')
            print('your total wallet is ', player_money)
            
            

        elif casino_dice > player_dice:
            player_money -= player_bet
            print(f'you lost {player_bet}!!!')
            print('your total wallet is ', player_money)
                

        return player_money
if __name__ == '__main__' :
    
    
    player_money = dice_game_starter(player_money)
    