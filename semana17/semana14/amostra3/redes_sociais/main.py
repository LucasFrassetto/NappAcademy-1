from redes_sociais import facebook, linkedin, github, instagram

if __name__ == "__main__":
    phrase = "Qual perfil deseja criar: "
    phrase += "[facebook], [linkedin], [github], [instagram]"
    profile_type = input(phrase)
    print(phrase)
    profile = eval(profile_type.lower())()
    print("Criando perfil... ", type(profile).__name__)
    print("Perfil possui as sessões", profile.getSections())
