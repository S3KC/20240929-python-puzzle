def main():
    final_answer = 1
    races = []

    with open('input.txt') as f:
        times = f.readline().strip().split()[1:]
        distances = f.readline().strip().split()[1:]

        for time_line, distance_line in zip(times, distances):
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
    with open('input.txt') as f:
        times = f.readline().strip().split()[1:]
        distances = f.readline().strip().split()[1:]

        # TASK 1: Use an algebraic model to quickly calculate the number of ways to win this race, without any loops.
        ways_to_win = 0

    # Task 2: Remove this line and return the number of ways to win for this race.
    raise NotImplementedError


if __name__ == '__main__':
    result = main()
    print(result)
