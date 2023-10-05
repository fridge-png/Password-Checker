"""


"""


from utils import checkCharacters,checkCommonPasswords,checkLength


def main():
    try:
        password = input("Input your password:\n")
        if not checkLength(password):
            print("Weak Password: Must be at least 8 characters long.")
            return 
        if not checkCharacters(password):
            print("Weak Password: Must include symbols, numbers, lowercase/uppercase letters.")
            return 
        if not checkCommonPasswords(password):
            print("Common Password: Found in a list of common passwords.")
            return 
        print ("Good Password!")
        return
    except Exception as error:
        print(f'Something went wrong: {error}')


if __name__ == "__main__":
    main()




        