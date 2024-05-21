import pytest 
from tarea import Tarea

@pytest.fixture
def tarea():
    return Tarea(1, "Programación", "Entregada")

def test_tarea(tarea):
    assert tarea.read() == "1, Programación, Entregada"