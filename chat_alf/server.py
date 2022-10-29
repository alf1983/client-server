import socket
import sys
import json
import common.consts as constants
from common.utils import get_message, send_message


def process_client_message(message):

    if constants.ACTION in message and message[constants.ACTION] == constants.PRESENCE and constants.TIME in message \
            and constants.USER in message:
        if message[constants.USER][constants.ACCOUNT_NAME] in constants.USERS:
            return {constants.RESPONSE: 200}
        return {
            constants.RESPONSE: 401,
            constants.ERROR: 'User \'' + message[constants.USER][constants.ACCOUNT_NAME] + '\' not recognized'
        }
    return {
        constants.RESPONSE: 400,
        constants.ERROR: 'Bad Request'
    }


def main():

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = constants.DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('Номер порта может быть указано только в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    transport_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    transport_server.bind((listen_address, listen_port))

    # Слушаем порт
    transport_server.listen(constants.MAX_CONNECTIONS)

    while True:
        client, client_address = transport_server.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
