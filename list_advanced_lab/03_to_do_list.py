def process_to_do_notes():
    to_do_notes = []

    while True:
        command = input()
        if command == 'End':
            break
        to_do_notes.append(command)
    
    sorted_notes = sorted(to_do_notes, key=lambda x: int(x.split('-')[0]))
    sorted_text = [note.split('-')[1] for note in sorted_notes]
    return sorted_text

result = process_to_do_notes()
print(result)