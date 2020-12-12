from collections import defaultdict


def ingest_file():
    with open("forms.txt") as forms:
        return forms.read().strip().split("\n\n")


def calculate_total_with_multiple_people(form):
    each_persons_answer = form.split("\n")
    total_number_of_people = len(each_persons_answer)
    answer_count = defaultdict(int)
    result = 0
    for answer in each_persons_answer:
        if len(answer) > 1:
            for letter in answer:
                answer_count[letter] += 1
        else:
            answer_count[answer] += 1
    return sum(1 for value in answer_count.values() if value == total_number_of_people)


if __name__ == "__main__":
    forms = ingest_file()
    total = 0
    for form in forms:
        if "\n" in form:
            total += calculate_total_with_multiple_people(form)
        else:
            total += len(form)
    print(total)
