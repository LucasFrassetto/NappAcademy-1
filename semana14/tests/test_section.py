from semana14.redes_sociais.sessoes import Section, PersonalSection, AlbumSection, PublicationSection, UploadCodeSection
import pytest
import unittest


class TestSessions(unittest.TestCase):
	def instace_object(self):
		obj = PersonalSection()
		assert isinstance(obj, PersonalSection)

	def test_personal_section(self):
		msg = 'Dados Pessoais'
		obj = PersonalSection()
		assert isinstance(obj, PersonalSection)
		assert obj.__repr__() == msg
		assert str(obj) == msg

	def test_album_section(self):
		msg = 'Sessão para fotos'
		obj = AlbumSection()
		assert isinstance(obj, AlbumSection)
		assert obj.__repr__() == msg
		assert str(obj) == msg

	def test_publication_section(self):
		msg = 'Sessão publicações'
		obj = PublicationSection()
		assert isinstance(obj, PublicationSection)
		assert obj.__repr__() == msg
		assert str(obj) == msg

	def test_upload_code_section(self):
		msg = 'Sessão upload code'
		obj = UploadCodeSection()
		assert isinstance(obj, UploadCodeSection)
		assert obj.__repr__() == msg
		assert str(obj) == msg