import pytest
from users.models import User

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username ='pepe',
        email = 'asd@gmail.com',
        password = '12345'
    )
    assert user.username == 'pepe'