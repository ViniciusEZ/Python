# I have a cat and a dog.
# I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now as [humanYears,catYears,dogYears]

def human_years_cat_years_dog_years(human_years):
    return [human_years, human_years * 15, human_years * 15] if human_years <= 1 else [human_years, human_years * 12, human_years * 12] if human_years == 2 else [human_years, 15 + 9 + (4 * (human_years - 2)), 15 + 9 + (5 * (human_years - 2))]

print(human_years_cat_years_dog_years(3))