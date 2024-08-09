Dataa = {
    'Urls': {
        'Index_url': '100_days_of_code',
        'DaysAuto_url': '100_days_of_code/days_auto',
        'Day1_url': '100_days_of_code/day1',
    },
    'Index': {
        'for_render': {
            'h1': '100 days of code Home Page!!!!'
        }
    },
    'DaysAuto': {
        
    },
    'Day1': {
        'url': 'day1',
        'for_render': {
            'h1': 'Day1 Challenge',
            'code': {
                'input': r"""
        print('Welcome to band name generator')
        user_name = input('enter your name: ')
        pet_name = input('enter your pet name: ')
        print(f'your band name could be {user_name} {pet_name}!!'),
                """,
                'output': r"""
        Welcome to band name generator
        enter your name: sanju 
        enter your pet name: jimmy
        your band name could be sanju  jimmy
                """
            }
        }
    }
}
# 