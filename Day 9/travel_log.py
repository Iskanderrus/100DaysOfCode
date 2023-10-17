travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon']
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart']
    },
]


def add_new_country(country: str, num_visits: int, cities: list):
    new_entry = {
        'country': country,
        'visits': num_visits,
        'cities': cities
    }
    travel_log.append(new_entry)
    print(travel_log)


add_new_country('Russia', 2, ['Moscow', 'SPb'])
for log in travel_log:
    print()
    for k, v in log.items():
        print(f"{k.title()}: {v}")