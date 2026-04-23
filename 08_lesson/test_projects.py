import pytest
from project_api import ProjectAPI
import datetime

BASE_URL = "https://ru.yougile.com" # Добавили ru.
TOKEN = "gRJOhVTXUueK40M2BH2j2wAcB8Nc+WKWOrmgv2DOhIw3wuyhfE82vrO21aCPbPFo"
COMPANY_ID = "89b920c8-400f-4623-9cf0-7a6ae1e00010"

@pytest.fixture
def api():
    # Теперь здесь ровно 3 аргумента (BASE_URL, TOKEN, COMPANY_ID)
    return ProjectAPI(BASE_URL, TOKEN, COMPANY_ID)

# Далее ваши тесты (без дубликатов!)
def test_create_project_positive(api):
    title = "Новый 123"
    response = api.create_project(title)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative_empty_title(api):
    response = api.create_project("")
    assert response.status_code == 400

def test_get_project_positive(api):
    res = api.create_project("Project to Get")
    project_id = res.json()["id"]
    response = api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Project to Get"

def test_get_project_negative_invalid_id(api):
    response = api.get_project("00000000-0000-0000-0000-000000000000")
    assert response.status_code in [404, 400]

def test_update_project_positive(api):
    project_id = api.create_project("Initial Title").json()["id"]
    response = api.update_project(project_id, "Updated Title")
    assert response.status_code == 200

def test_update_project_negative_non_existent(api):
    response = api.update_project("00000000-0000-0000-0000-000000000000", "Title")
    assert response.status_code in [404, 400]