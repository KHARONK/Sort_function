from operator import indexOf
import sys
from SortFunctions import quick_sort
import random
import csv


def main():
    filename="movies.csv"
    movies_by_genre = []
    try:
        with open(filename, newline="\n",encoding="utf8") as csvfile:
            movie_reader = csv.reader(csvfile, delimiter=",",quotechar='"',quoting=csv.QUOTE_ALL,skipinitialspace=True,strict=True)
            for row in movie_reader:
                movies_by_genre.append((row[2].split("|")[0], row[1]))
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, movie_reader.line_num, e))

    sorted_genre = quick_sort(0, len(movies_by_genre) - 1, movies_by_genre)

    try:
        with open("sorted.csv", 'w') as sorted_file:
            sorted_writer = csv.writer(sorted_file)
            sorted_writer.writerows(sorted_genre)
        with open("unsorted.csv", 'w') as unsorted_file:
            unsorted_writer = csv.writer(unsorted_file)
            unsorted_writer.writerows(movies_by_genre)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, movie_reader.line_num, e))

    index = random.randint(0, len(sorted_genre) - 1)

    accepted_inputs = [3, 4, 5, 6, 7]

    choice = input(
        "How many movie recommendations do you want?\n\n You are to choose from 3 to 7.\n"
    )

    choice = int(choice.strip())

    if choice not in accepted_inputs:
        choice = 3

    chosen_genre = sorted_genre[index][0]

    chosen_genre_list = list(filter(lambda mv : mv[0] == chosen_genre, sorted_genre))

    random.shuffle(chosen_genre_list)

    recommendations = []

    i = 0
    while i < choice:
        if i >= len(chosen_genre_list):
            break
        recommendations.append(chosen_genre_list[i])
        i+=1

    return recommendations      


if __name__ == "__main__":
    print(main())
