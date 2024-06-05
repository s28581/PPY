class Date:
    def __init__(self, day, month, year):
        if not (1 <= day <= 31):
            raise ValueError(f"Day {day} is out of range (1-31)")
        if not (1 <= month <= 12):
            raise ValueError(f"Month {month} is out of range (1-12)")
        if not (year >= 1):
            raise ValueError(f"Year {year} is not supported, should be greater than 1")

        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, date):
        return (self.year, self.month, self.day) < (date.year, date.month, date.day)

    def __eq__(self, date):
        return (self.year, self.month, self.day) == (date.year, date.month, date.day)

    def __str__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"


class Note:
    def __init__(self, id, date, text):
        self.id = id
        self.date = date
        self.text = text


class Calendar:
    def __init__(self):
        self.notes = []
        self.id = 1

    def add_note(self, day, month, year, text):
        try:
            date = Date(day, month, year)
            note = Note(self.id, date, text)
            self.notes.append(note)
            self.id += 1
        except ValueError as value_err:
            print(value_err)

    def remove_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]

    def show_notes(self):
        for note in sorted(self.notes, key=lambda n: n.date):
            print(f"{note.id} {note.date} {note.text}")

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for note in sorted(self.notes, key=lambda n: n.date):
                file.write(f"{note.id} {note.date} {note.text}\n")


calendar = Calendar()
calendar.add_note(10, 5, 2023, "Note 1")
calendar.add_note(22, 12, 2022, "Note 2")
calendar.add_note(5, 1, 2024, "Note 3")

try:
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    text = input("Enter text for the note: ")
    calendar.add_note(day, month, year, text)
except ValueError as value_err:
    print(value_err)

print("\nNotes in chronological order:")
calendar.show_notes()

calendar.write_to_file("notes.txt")
