from Users.player import Player
from basicdicegame import dice_game_starter, play_again_quest
from Users.log_in import LogIn

login = LogIn()

while login.is_account_ready == False:
    login = LogIn()
    
username = login.username[:]
player = Player(username)
del login


game_options = ['dice_game']


chosen_game = input('which game you want to play d or q')
while chosen_game.lower() in ['d','q']:
    chosen_game = input('you have got to tell me properly that what you want to play')

if chosen_game.lower() == 'd':
    play_again = True
    while play_again == True:
        player.wallet.capital = dice_game_starter(player.wallet.capital)
        player.wallet.update_capital_json(player.wallet.capital)
        play_again = play_again_quest(player.wallet.capital)


print('userWallet in main.py',player.wallet.capital)




















    