from redes_sociais import facebook, linkedin, github, instagram


if __name__ == "__main__":
    profile_type = input(
        "Qual perfil deseja criar: [facebook], [linkedin], [github], [instagram]")
    profile = eval(profile_type.lower())()
    print("Criando perfil... ", type(profile).__name__)
    print("Perfil possui as sessões", profile.getSections())
