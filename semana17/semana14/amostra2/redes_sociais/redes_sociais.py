from abc import ABC, abstractmethod
from redes_sociais.sessoes import PersonalSection, AlbumSection, PublicationSection, UploadCodeSection


class Profile(ABC):
    def __init__(self):
        self._sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self._sections

    def addSections(self, section):
        self._sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


class github(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(UploadCodeSection())


class instagram(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
