PASSING_GRADE = 75


def get_scores():
    scores = []
    count = int(input("How many subjects? "))
    for i in range(count):
        while True:
            try:
                score = float(input(f"Grade for subject {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a number.")
    return scores


def get_rating(average):
    if average >= 90:
        return "Excellent"
    elif average >= 85:
        return "Very Good"
    elif average >= 80:
        return "Good"
    elif average >= PASSING_GRADE:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def main():
    print("=== Grade Calculator ===")
    scores = get_scores()
    average = sum(scores) / len(scores)
    print(f"Average: {average:.2f}")
    print(f"Rating: {get_rating(average)}")

    if average >= PASSING_GRADE:
        print("Remarks: PASSED")
    else:
        print("Remarks: FAILED")


if __name__ == "__main__":
    main()
