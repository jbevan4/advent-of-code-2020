def ingest_file():
    with open("forms.txt") as forms:
        return [line.replace("\n", "") for line in forms.read().split("\n\n")]


if __name__ == "__main__":
    forms = ingest_file()
    print(sum(len(set(form)) for form in forms))
