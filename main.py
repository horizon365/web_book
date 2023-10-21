import os

for path in os.listdir('.'):
    if not path.startswith('.') and os.path.isdir(path):
        os.chdir(path)
        rename = path.replace(' ', '')
        new_name = f'./{rename}.epub'
        if os.path.isfile(new_name):
            continue
        os.system('gitbook-plugin-summary.py . -o')
        os.system('gitbook init')
        os.system(f'gitbook epub ./ {new_name}')
        os.chdir('..')

name = ''
for path in os.listdir('.'):
    if not path.startswith('.') and os.path.isdir(path):
        rename = path.replace(' ', '')
        name += f'<{rename}>'
print(name)
