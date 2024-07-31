import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(99, 'teste')
        encrypt_message('teste', None)

    assert encrypt_message('texto', 6) == 'otxet'
    assert encrypt_message('texto', -2) == 'otxet'
    assert encrypt_message("mensagem", 5) == "asnem_meg"
    assert encrypt_message("mensagem", 4) == "mega_snem"