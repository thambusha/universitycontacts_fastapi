# university_contacts_agent.py

university_contacts = {
    "Harvard University": {
        "Phone": "+1 617-495-1000",
        "Email": "info@harvard.edu",
        "Website": "https://www.harvard.edu"
    },
    "Stanford University": {
        "Phone": "+1 650-723-2300",
        "Email": "info@stanford.edu",
        "Website": "https://www.stanford.edu"
    },
    "University of Oxford": {
        "Phone": "+44 1865 270000",
        "Email": "information.office@admin.ox.ac.uk",
        "Website": "https://www.ox.ac.uk"
    }
}

def get_contact(university_name):
    contact = university_contacts.get(university_name)
    if contact:
        return f"\nContact for {university_name}:\n" + "\n".join(f"{k}: {v}" for k, v in contact.items())
    else:
        return "Sorry, university not found. Try another name."

def main():
    print("Welcome to the University Contact Info Agent")
    while True:
        uni_name = input("\nEnter university name (or 'exit' to quit): ")
        if uni_name.lower() == 'exit':
            break
        print(get_contact(uni_name))

if __name__ == "__main__":
    main()
