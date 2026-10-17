PASSING_GRADE = 75


def get_scores():
    scores = []
    count = int(input("How many subjects? "))
    for i in range(count):
        score = float(input(f"Grade for subject {i + 1}: "))
        scores.append(score)
    return scores


def main():
    print("=== Grade Calculator ===")
    scores = get_scores()
    average = sum(scores) / len(scores)
    print(f"Average: {average:.2f}")

    if average >= PASSING_GRADE:
        print("Remarks: PASSED")
    else:
        print("Remarks: FAILED")


if __name__ == "__main__":
    main()
