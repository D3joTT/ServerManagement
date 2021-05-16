import os
from pathlib import Path

directories = ['lobby1', 'lobby2', 'lobby3']


def update():
    files = get_files('./toUpdate')
    for directory in directories:
        for to_update in files:
            file = Path(f'./../{directory}/plugins/{to_update}')
            if file.exists():
                os.system(f'rm -r ./../{directory}/plugins/{to_update}')
            os.system(f'cp -R ./toUpdate/{to_update} ./../{directory}/plugins')
    print(f' \n Pomyslnie zmodyfikowano: {files}\n')


def get_files(route):
    files = []
    for f in os.listdir(route):
        files.append(f)
    return files


update()
