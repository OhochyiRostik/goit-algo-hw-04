def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments."
    
    name, phone = args
    if name in contacts:
        return "Contact already exists."

    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments."
    
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    # For one or more contacts

    result = []
    for i in args:
        result.append(f"{i} - {contacts.get(i)}")
    return "\n".join(result)

def show_all(contacts):
    result = []
    for key, value in contacts.items():
        result.append(f"{key} - {value}")
    return "\n".join(result)
