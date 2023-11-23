def main():
    # Ask user for a list of student scores
    student_scores = input("Input a list of student scores: ").split(" ")
    # find the highest scores in the list
    print(f"The highest score in the class is: {get_highest_score(student_scores)}")


def get_highest_score(scores):
    """

    :param scores:
    :return:
    """
    high_score = 0
    for score in scores:
        score = int(score)
        if score > high_score:
            high_score = score
    return high_score


main()
