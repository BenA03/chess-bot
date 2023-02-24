import re
import random

def handle_response(user_message, history) -> str:

    valid_move = re.compile(r'[QKNBR]?x?[a-h][1-9][+#]?')

    user_message = user_message[3:]

    if user_message == 'help':
        return 'Type **!c play** to start a game'

    if user_message == 'play':
        return 'Cool! Let\'s play a game! Use !c [move notation] to send your first move.'
    
    if '!c play' not in history:
        return 'We haven\'t started a game. Type **!c play** to start a game, or **!c help** for help'
    
    if valid_move.search(user_message) or user_message == 'O-O' or user_message == 'O-O-O':
        return f"Ok, you played {user_message}. I'll play e5."
    else:
        return user_message