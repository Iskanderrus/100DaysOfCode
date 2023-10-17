height = float(input('Height of the wall in m: '))
width = float(input('Width of the wall in m: '))
coverage = float(input('How many square meters of wall can be covered by one can of your paint?\n'))


def paint_calc(height, width, coverage):
    """
    Calculating number of cans needed to paint certain area
    :param height: Height in meters
    :param width: Width in meters
    :param coverage: How many square meters can be painted by just one can
    :return: None. Print the statement based on whether the number of cans is a whole number.
    """
    area = height * width
    cans = round(area / coverage, 2)
    if cans.is_integer():
        print(f'With your paint you would need exactly {int(cans)} cans to make the job.')
    else:
        print(
            f'With your paint you would need approximately {cans} cans to make the job.')


paint_calc(height, width, coverage)
