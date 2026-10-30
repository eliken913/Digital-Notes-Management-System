import os

FILE_NAME = "notes.txt"


# STEP 1: Load all notes from file
def load_notes():
    notes = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|", 2)

                    if len(parts) == 3:
                        note = {
                            "id": parts[0],
                            "title": parts[1],
                            "content": parts[2]
                        }
                        notes.append(note)

    return notes


# STEP 2: Save all notes into file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        for note in notes:
            file.write(
                note["id"] + "|" +
                note["title"] + "|" +
                note["content"] + "\n"
            )


# STEP 3: Generate new Note ID
def generate_id(notes):
    max_number = 0

    for note in notes:
        number = int(note["id"][1:])

        if number > max_number:
            max_number = number

    return "N" + str(max_number + 1)


# STEP 4: Add a new note
def add_note(notes):
    title = input("Enter note title: ").strip()

    if title == "":
        print("Title cannot be empty. Note not saved.")
        return

    content = input("Enter note content: ").strip()

    if "|" in title or "|" in content:
        print("Please do not use | in title or content.")
        return

    note_id = generate_id(notes)

    note = {
        "id": note_id,
        "title": title,
        "content": content
    }

    notes.append(note)
    save_notes(notes)

    print("Note saved. ID:", note_id, "|", title)


# STEP 5: View all notes
def view_notes(notes):
    if len(notes) == 0:
        print("No notes found.")
        return

    print("\n========== ALL NOTES ==========")

    for note in notes:
        print(
            note["id"], "|",
            note["title"], "|",
            note["content"]
        )

    print("================================")


# STEP 6: Search notes
def search_notes(notes):
    keyword = input("Enter keyword to search: ").strip().lower()

    if keyword == "":
        print("Please enter a search keyword.")
        return

    found = False

    for note in notes:
        if (keyword in note["title"].lower()
                or keyword in note["content"].lower()):

            print(
                note["id"], "|",
                note["title"], "|",
                note["content"]
            )

            found = True

    if not found:
        print("No matching notes found.")


# STEP 7: Edit a note
def edit_note(notes):
    note_id = input("Enter Note ID to edit: ").strip().upper()

    for note in notes:
        if note["id"] == note_id:

            new_content = input("Enter new content: ").strip()

            if "|" in new_content:
                print("Please do not use | in content.")
                return

            note["content"] = new_content

            save_notes(notes)

            print("Note", note_id, "updated.")
            return

    print("Note ID does not exist.")


# STEP 8: Delete a note
def delete_note(notes):
    note_id = input("Enter Note ID to delete: ").strip().upper()

    for note in notes:
        if note["id"] == note_id:

            notes.remove(note)
            save_notes(notes)

            print(
                "Note", note_id,
                "deleted. Notes left:", len(notes)
            )
            return

    print("Note ID does not exist.")


# STEP 9: Main Menu
def main():

    notes = load_notes()

    while True:

        print("\n===== DIGITAL NOTES MANAGEMENT SYSTEM =====")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            search_notes(notes)

        elif choice == "4":
            edit_note(notes)

        elif choice == "5":
            delete_note(notes)

        elif choice == "6":
            print("Thank you for using Digital Notes Management System!")
            break

        else:
            print("Invalid choice. Please enter 1 to 6.")


# STEP 10: Start the program
if __name__ == "__main__":
    main()