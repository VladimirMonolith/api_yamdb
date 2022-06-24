from enum import Enum


class UserRoles(Enum):
    """Класс-перечисление для выбора пользовательских ролей."""

    user = 'user'
    moderator = 'moderator'
    admin = 'admin'

    @classmethod
    def choices(cls):
        """Формирует соответствие констант и значений."""
        return tuple((attribute.name, attribute.value) for attribute in cls)
