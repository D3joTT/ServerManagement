import os
from pathlib import Path

directories = ['lobby1', 'lobby2', 'lobby3']


def update():
    for directory in directories:
        files = get_files('./toUpdate')
        for to_update in files:
            file = Path(f'./../{directory}/plugins/{to_update}')
            if file.exists():
                os.system(f'rm -r ./../{directory}/plugins/{to_update}')
            os.system(f'cp -R {to_update} ./../{directory}/plugins')


def get_files(route):
    files = []
    for f in os.listdir(route):
        files.append(f)
    return files


update()
