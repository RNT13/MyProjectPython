import pytest
import os
from django.urls import reverse
from .factories import PostFactory

# ==================
# Testes de View
# ==================


@pytest.mark.django_db
def test_post_list_view(client):
    """Verifica se a view principal do blog retorna status 200."""
    url = reverse('blog:home')
    response = client.get(url)
    assert response.status_code == 200

# ==================
# Testes de Modelo/Factory
# ==================


@pytest.fixture
def post_published():
    """Fixture que cria um post usando a factory."""
    return PostFactory(title="pytest with factory")


@pytest.mark.django_db
def test_create_published_post(post_published):
    """Verifica se a factory cria um post com o título correto."""
    assert post_published.title == "pytest with factory"
