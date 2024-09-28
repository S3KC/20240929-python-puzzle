def main():
    final_answer = 0
    races = []

    with open('input.txt') as f:
        time_lines = f.readline().strip().split()[1:]
        distance_lines = f.readline().strip().split()[1:]

        for time_line, distance_line in zip(time_lines, distance_lines):
            time = int(time_line.strip())
            distance = int(distance_line.strip())
            races.append((time, distance))

    # TASK 1: Calculate the number of ways to win for each race, using the races list which has the following format:
    # races = [
    #     (time1, distance1),
    #     (time2, distance2),
    #     ...
    # ]

    return final_answer


def challenge():
    pass


if __name__ == '__main__':
    result = main()
    print(result)
