def name_formatter(first_name: str, last_name: str, *middle_names: str) -> str:
    """
    Basic function to format username deleting excessive spaces and capitalizing the first letter of both parts.
    :param first_name: First name of the user
    :param last_name: Last name of the user
    :param middle_names: Middle name(s) of the user
    :return: String of formatted user full name
    """
    # Capitalize and strip spaces for first name and last name
    formatted_first_name = first_name.strip().title()
    formatted_last_name = last_name.strip().title()

    # Check if middle names exist and concatenate the full name accordingly
    if middle_names:
        formatted_middle_names = ' '.join([name.strip().title() for name in middle_names[0].split(' ') if name != ''])
        full_name = f'{formatted_first_name} {formatted_middle_names} {formatted_last_name}'
    else:
        full_name = f'{formatted_first_name} {formatted_last_name}'

    return full_name


# Test cases
print(name_formatter('   AlexanDER', '          ChAsOvSkOy', 'NiKoLaYEvich'))
print(name_formatter('   AlexanDER', '          ChAsOvSkOy'))
print(name_formatter('   AlexanDER', '          ChAsOvSkOy',
                     'NiKoLaYEvich          Abdelsalekh Elena    Maria     Garcia'))