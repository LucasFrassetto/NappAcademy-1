from abc import ABC, abstractmethod


class Section(ABC):
    @abstractmethod
    def sobre(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class PersonalSection(Section):
    def __init__(self):
        self._posts = []

    def sobre(self):
        print("Sessao para dados pessoais")

    def __str__(self):
        return 'Dados Pessoais'

    def __repr__(self):
        return 'Dados Pessoais'


class AlbumSection(Section):
    def sobre(self):
        print("Sessao para fotos")

    def __str__(self):
        return 'Sessão para fotos'

    def __repr__(self):
        return 'Sessão para fotos'


class PublicationSection(Section):
    def describe(self):
        print("Sessao para Publicações")

    def sobre(self):
        print("Sessao para publicações(posts)")

    def __str__(self):
        return 'Sessão publicações'

    def __repr__(self):
        return 'Sessão publicações'


class UploadCodeSection(Section):
    def sobre(self):
        print("Sessao para upload de dados")

    def upload(self):
        print("Sessão para Upload")

    def __str__(self):
        return 'Sessão Upload'

    def __repr__(self):
        return 'Sessão Upload'
