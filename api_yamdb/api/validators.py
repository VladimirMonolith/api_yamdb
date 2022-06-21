from rest_framework import serializers


def no_me_username(data):
    """Запрещает пользователям изменять себе имя на me."""
    if data.get('username') == 'me':
        raise serializers.ValidationError(
            'Использовать имя me запрещено'
        )
    return data
