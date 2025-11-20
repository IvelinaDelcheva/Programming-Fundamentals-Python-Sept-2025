while True:
    text = input()
    reversed_text = ''
    if text == 'end':
        break

    for ch in reversed(text):
        reversed_text += ch
    
    print(f'{text} = {reversed_text}')