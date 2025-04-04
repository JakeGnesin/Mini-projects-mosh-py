while True:
    filename = input('Enter file name: ')
    if '\\' in filename:
        print('Invalid file name')
    else:
        print(f'You entered {filename}')
        break

print('Enter your text below (type SAVE on a new line to save and exit):')
text_lines = []
while True:
    line = input()
    if line.strip().upper() == 'SAVE':
        # Save the file
        try:
            with open(filename, 'w') as file:
                file.write('\n'.join(text_lines))
            print(f'File saved as {filename}')
            break
        except Exception as e:
            print(f'Error saving file: {e}')
            break
    else:
        text_lines.append(line)
