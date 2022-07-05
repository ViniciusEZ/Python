import os

caminho_search = input('Type a path: ')
termo_search = input('Type a term: ')

def format_size(size):
    base = 1000
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'
    size = round(size, 2)
    return f'{size}{text}'

c = 0
for root, directories, files in os.walk(caminho_search):
    for file in files:
        if termo_search in file:
            try:
                c += 1
                full_path = os.path.join(root, file)
                file_name, file_ext = os.path.splitext(file)
                size = os.path.getsize(full_path)
                print()
                print(f'Found the file: {file}')
                print(f'Path: {full_path}')
                print(f'Name: {file_name}')
                print(f'Extension: {file_ext}')
                print(f'Size: {size}')
                print(f'Formated Size: {format_size(size)}')
            except PermissionError as e:
                print('No permission')
            except FileNotFoundError:
                print('File not found')
            except Exception as e:
                print(f'Unknow error: {e}')

print()
print(f'{c} file(s) found')