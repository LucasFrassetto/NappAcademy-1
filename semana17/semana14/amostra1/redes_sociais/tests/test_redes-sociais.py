# -*- coding: utf-8 -*-
from redes_sociais import linkedin, facebook, github, instagram
from sessoes import PersonalSection, PublicationSection, AlbumSection, Section, UploadCode


import pytest


class TestSessoes:
	def test_class_personalSession(self):
		msg = 'Dados Pessoais'
		objeto = PersonalSection()
		assert isinstance(objeto, PersonalSection)
		assert objeto.__str__() == msg
		assert objeto.__repr__() == msg

	def test_class_AlbumSection(self):
		msg = 'Sessão para fotos'
		objeto = AlbumSection()
		assert isinstance(objeto, AlbumSection)
		assert objeto.__str__() == msg
		assert objeto.__repr__() == msg

	def test_class_PublicationSection(self):
		msg = 'Sessão publicações'
		objeto = PublicationSection()
		assert isinstance(objeto, PublicationSection)
		assert objeto.__str__() == msg
		assert objeto.__repr__() == msg

	def test_class_UploadCode(self):
		msg = 'Sessão codigos'
		objeto = UploadCode()
		assert isinstance(objeto, UploadCode)
		assert objeto.__str__() == msg
		assert objeto.__repr__() == msg

	def test_class_Section(self):
		msg_erro = "Can't instantiate abstract class Section with abstract methods __repr__, __str__, sobre"
		with pytest.raises(TypeError) as error:
			Section()
		assert str(error.value) == msg_erro

class TestRedesSociais:
	def test_class_linkedin(self):
		objeto = linkedin()
		assert isinstance(objeto, linkedin)
		profile_type = 'linkedin'
		profile = eval(profile_type.lower())()
		assert str(profile.getSections()) == '[Dados Pessoais, Sessão publicações]'

	def test_class_facebook(self):
		objeto = facebook()
		assert isinstance(objeto, facebook)
		profile_type = 'facebook'
		profile = eval(profile_type.lower())()
		assert str(profile.getSections()) == '[Dados Pessoais, Sessão para fotos]'

	def test_class_github(self):
		objeto = github()
		assert isinstance(objeto, github)
		profile_type = 'github'
		profile = eval(profile_type.lower())()
		assert str(profile.getSections()) == '[Dados Pessoais, Sessão codigos]'

	def test_class_instagram(self):
		objeto = instagram()
		assert isinstance(objeto, instagram)
		profile_type = 'instagram'
		profile = eval(profile_type.lower())()
		assert str(profile.getSections()) == '[Dados Pessoais, Sessão publicações]'