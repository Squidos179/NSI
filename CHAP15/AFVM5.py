liste = ['Aubree', '26', '06', 'Squidos']

def bruteforce(word, length):
    if length <= 5:
        for letter in liste:
            if mdp == word + letter:
                print("Votre mot de passe est " + word + letter)
            else:
                print(word + letter)
                bruteforce(word + letter, length + 1)



mdp = input("Entrez votre mot de passe : ")
bruteforce('', 1)