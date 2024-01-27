import keyboard

def capture_input():
    if keyboard.is_pressed('up'):
        return 'UP'
    elif keyboard.is_pressed('down'):
        return 'DOWN'
    elif keyboard.is_pressed('left'):
        return 'LEFT'
    elif keyboard.is_pressed('right'):
        return 'RIGHT'
    return ''
