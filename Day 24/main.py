# בס״ד

from pathlib import Path

# Reading names from the file
names_path = Path('./customers/names.txt')
names_contents = names_path.read_text()
names = names_contents.splitlines()

# Reading message blueprint
blueprint_path = Path('./input/blueprint.txt')
blueprint = blueprint_path.read_text()

# Generating personalized message and saving it to the individual file
for name in names:
    # replacing the placeholder
    message = blueprint.replace('[NAME]', str(name))
    # creating individual path
    path = Path(f'output/letter_for_{name}.txt')
    # create empty file
    path.touch()
    # writing the personalized message into individual file
    path.write_text(message)
