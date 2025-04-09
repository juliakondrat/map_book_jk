def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user ['location']} opublikowało {user["posts"]}')


def add_user(users_data: list) -> None:
    new_name: str = input('podaj imię nowego znajomego: ')
    new_location: str = input('Podaj nazwę lokalizacji: ')
    new_posts: int = int(input('Podaj liczbę postów:'))
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts}, )
