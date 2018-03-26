def make_get_token_url(client_id):
    get_token_url = 'https://oauth.yandex.ru/authorize'
    get_token_params = f'response_type=token&client_id={client_id}'

    return f'{get_token_url}?{get_token_params}'


def core(client_id):
    get_token_url = make_get_token_url(client_id)
    print(get_token_url)


if __name__ == '__main__':
    core('9d452a0a0ec64c7c8f16c08bd83ea097')
    # { TOKEN: AQAAAAANuCzYAATopEPaH7-Ma0xMjVIr9SiEw3o }
