import os

screen = 'bungeecord'

os.system(f'screen -dmS {screen} java -Xms3G -Xmx3G -jar {screen}.jar nogui')

print('\n      ================================\n')
print(f'       Uruchomiony screen: {screen}\n')
print('      ================================\n')
