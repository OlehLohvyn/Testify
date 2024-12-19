from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Тут можна додавати додаткові поля
    pass
