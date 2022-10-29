import sys
import json
import socket
import time
import common.consts as constants
from common.utils import get_message, send_message


def create_presence(account_name):
    out = {
        constants.ACTION: constants.PRESENCE,
        constants.TIME: time.time(),
        constants.USER: {
            constants.ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):

    if constants.RESPONSE in message:
        if message[constants.RESPONSE] == 200:
            return '200 : OK'
        return f'{message[constants.RESPONSE]} : {message[constants.ERROR]}'
    raise ValueError


def main():

    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = constants.DEFAULT_IP_ADDRESS
        server_port = constants.DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)
    client_name = constants.DEFAULT_USER
    if '-u' in sys.argv:
        client_name = sys.argv[sys.argv.index('-u') + 1]
    if '-user' in sys.argv:
        client_name = sys.argv[sys.argv.index('-user') + 1]

    transport_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport_client.connect((server_address, server_port))
    message_to_server = create_presence(client_name)
    send_message(transport_client, message_to_server)
    try:
        answer = process_ans(get_message(transport_client))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
