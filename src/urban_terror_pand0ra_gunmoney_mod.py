import datetime
import re
import socket
import time

import pygame


def play_audio(file_path):
    pygame.mixer.init()

    pygame.mixer.music.load(file_path)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def parse_map_name(text):
    found = re.search(r'mapname\\([^\\]+)', text)
    if found:
        return found.group(1)
    return None


def filter_players(player):
    split_row = player.split(' ')
    if len(split_row) < 2:
        return False
    return split_row[1] != '0'


if __name__ == '__main__':
    while True:
        print(datetime.datetime.now())
        host = '94.130.173.8'
        port = 27961

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((host, port))

        sock.send('\xFF\xFF\xFF\xFFgetstatus'.encode('latin1', 'ignore'))
        result = sock.recv(5120).decode('utf-8', 'replace').split('\n')

        map_name = parse_map_name(result[1])
        print(f'map : {map_name}')
        print('| Score | Ping | Player |')
        players = list(filter(filter_players, result[2:]))
        print('\n'.join(players))
        print()

        for player in players:
            if 'NO' in player:
                play_audio('resources/audio/sound1.mp3')
        if players is None:
            play_audio('resources/audio/sound1.mp3')
        time.sleep(2)