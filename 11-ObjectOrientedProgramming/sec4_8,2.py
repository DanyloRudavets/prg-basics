from sec4_81 import Contact_list

def main():
    
    contact_list = Contact_list()

    # Add the provided contacts
    contact_list.add("John Brown", "brown@onet.pl", "555234000")
    contact_list.add("Anna May", "am@o2.pl", "232000199")
    contact_list.add("George Small", "smallg@google.pl", "222999100")
    contact_list.add("Paola Big", "bigpaola@poczta.pl", "100200300")

    # Display the contact list
    print("Contact List:")
    contact_list.display()

if __name__ == "__main__":
    main()
