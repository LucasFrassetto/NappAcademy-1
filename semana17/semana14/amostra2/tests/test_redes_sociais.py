import pytest
from redes_sociais.redes_sociais import facebook, linkedin, github, instagram
from redes_sociais.sessoes import AlbumSection, PersonalSection, PublicationSection, UploadCodeSection

class TestFacebook:
    def test_instanciar_facebook(self):
        objeto = facebook()
        assert isinstance(objeto, facebook)
        
class TestLinkedin:
    def test_instanciar_linkedin(self):
        objeto = linkedin()
        assert isinstance(objeto, linkedin)
        
class TestGithub:
    def test_instanciar_github(self):
        objeto = github()
        assert isinstance(objeto, github)
        
class TestInstagram:
    def test_instanciar_instagram(self):
        objeto = instagram()
        assert isinstance(objeto, instagram)
        
class TestName:
    def test_tipo_errado(self):
        profile_type = 'tdd'
        msg = f"name '{profile_type}' is not defined"
        with pytest.raises(NameError) as error:
            profile = eval(profile_type.lower())()
        assert str(error.value) == msg
        
    def test_tipo_certo_facebook(self):
        profile_type = 'facebook'
        profile = eval(profile_type.lower())()
        assert (type(profile).__name__) == 'facebook'
        profile = facebook().getSections()
        assert (str(profile)) == '[Dados Pessoais, Sessão para fotos]'
        
    def test_tipo_certo_linkedin(self):
        profile_type = 'linkedin'
        profile = eval(profile_type.lower())()
        assert (type(profile).__name__) == 'linkedin'
        profile = linkedin().getSections()
        assert (str(profile)) == '[Dados Pessoais, Sessão publicações]'
        
    def test_tipo_certo_github(self):
        profile_type = 'github'
        profile = eval(profile_type.lower())()
        assert (type(profile).__name__) == 'github'
        profile = github().getSections()
        assert (str(profile)) == '[Dados Pessoais, Sessão Upload]'
        
    def test_tipo_certo_intagram(self):
        profile_type = 'instagram'
        profile = eval(profile_type.lower())()
        assert (type(profile).__name__) == 'instagram'
        profile = instagram().getSections()
        assert (str(profile)) == '[Dados Pessoais, Sessão para fotos]'
