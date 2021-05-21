from semana14.redes_sociais.redes_sociais import Profile, linkedin, facebook, github, instagram
from semana14.redes_sociais.sessoes import PersonalSection, AlbumSection, PublicationSection, UploadCodeSection
import pytest
import unittest


class TestSocialNetworks(unittest.TestCase):
	def instace_object(self):
		obj = linkedin()
		assert isinstance(obj, linkedin)
		assert isinstance(obj, Profile)

	def test_linkedin(self):
		obj = linkedin()
		assert isinstance(obj, linkedin)
		assert isinstance(obj, Profile)
		obj.createProfile()
		sections = obj.getSections()
		assert isinstance(sections[0], PersonalSection)
		assert isinstance(sections[1], PublicationSection)

	def test_facebook(self):
		obj = facebook()
		assert isinstance(obj, facebook)
		assert isinstance(obj, Profile)
		obj.createProfile()
		sections = obj.getSections()
		assert isinstance(sections[0], PersonalSection)
		assert isinstance(sections[1], AlbumSection)

	def test_github(self):
		obj = github()
		assert isinstance(obj, github)
		assert isinstance(obj, Profile)
		obj.createProfile()
		sections = obj.getSections()
		assert isinstance(sections[0], PersonalSection)
		assert isinstance(sections[1], UploadCodeSection)

	def test_instagram(self):
		obj = instagram()
		assert isinstance(obj, instagram)
		assert isinstance(obj, Profile)
		obj.createProfile()
		sections = obj.getSections()
		assert isinstance(sections[0], PersonalSection)
		assert isinstance(sections[1], AlbumSection)
		assert isinstance(sections[2], PublicationSection)