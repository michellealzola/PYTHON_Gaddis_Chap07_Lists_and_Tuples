def get_population():
    infile = open('USPopulation.txt', 'r')
    population = infile.readlines()
    infile.close()
    for i in range(len(population)):
        population[i] = int(population[i].rstrip('\n'))
    return population


def get_total_population(population):
    total = 0
    for values in population:
        total += values
    return total


def get_average_population(population, total_population):
    return float(total_population / len(population))


def get_year_highest(population):
    highest_population = max(population)
    print(f'The highest population increase: {highest_population:,d}')
    highest_year = population.index(highest_population) + 1950
    return highest_year


def get_year_lowest(population):
    lowest_population = min(population)
    print(f'The lowest population increase: {lowest_population:,d}')
    lowest_year = population.index(lowest_population) + 1950
    return lowest_year


def main():
    population = get_population()
    total_population = get_total_population(population)
    print(f'The total US population from 1950 to 1990 is {total_population:,d}')
    average_population = get_average_population(population, total_population)
    print(f'The average US population from 1950 to 1990 is {average_population:,.2f}')
    year_highest = get_year_highest(population)
    print(f'The year with the highest increase in US population from 1950 to 1990 is {year_highest}')
    year_lowest = get_year_lowest(population)
    print(f'The year with the lowest increase in US population from 1950 to 1990 is {year_lowest}')


if __name__ == '__main__':
    main()
