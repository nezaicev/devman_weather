import requests

URL_PARAMS = {'nTq': '', 'lang': 'ru'}


def get_weather(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    print(get_weather('http://wttr.in/Лондон', URL_PARAMS))
    print(get_weather('http://wttr.in/Череповец', URL_PARAMS))
    print(get_weather('http://wttr.in/Шереметьево', URL_PARAMS))


if __name__ == "__main__":
    main()
