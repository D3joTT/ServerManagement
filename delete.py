import os
from pathlib import Path

directories = ['lobby1', 'lobby2', 'lobby3']


def delete(to_delete):
    for directory in directories:
        file = Path(f'./../{directory}/plugins/{to_delete}')
        if file.exists():
            os.system(f'rm -r ./../{directory}/plugins/{to_delete}')


delete('vulcan.jar')
