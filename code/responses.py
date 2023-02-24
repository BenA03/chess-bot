import re
import random

def handle_response(user_message, history) -> str:

    valid_move = re.compile(r'[QKNBR]?x?[a-h][1-9][+#]?')

    user_message = user_message[3:]

    if user_message == 'help':
        return 'Type **!c play** to start a game! I am a case-sensitive bot.'

    if user_message == 'play':
        return 'Cool! Let\'s play a game! Use !c [move notation] to send your first move.'
    
    if '!c play' not in history:
        return 'We haven\'t started a game. Type **!c play** to start a game, or **!c help** for help'
    
    if user_message == 'end':
        history.clear()
        return "Ok, I've cancelled out game. GG!"
    
    if valid_move.search(user_message) or user_message == 'O-O' or user_message == 'O-O-O':
        num = random.randint(1, 7)
        match num:
            case 1: 
                return f"Ok, you played {user_message}. I'll play e5, matching you in the center"
            case 2: 
                return f"Ok, you played {user_message}. I'll play d5, striking back in the center"
            case 3: 
                return f"Ok, you played {user_message}. I'll play Nf6"
            case 4: 
                return f"Ok, you played {user_message}. I'll play Nc6"
            case 5: 
                return f"Ok, you played {user_message}. I'll play Ke7, developing my king"
            case 6: 
                history.clear()
                return f"Ok, you played {user_message}. I'll play Qf2#, mating your king. Good game!"
            case 7: 
                return f"Ok, you played {user_message}. I'll play b6, preparing my bishop for development."
    else:
        return "Sorry, either your command is invalid, or I am not familiar with this chess notation. Please try again."