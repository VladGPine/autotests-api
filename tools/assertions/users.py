from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')


def assert_user(actual_user: UserSchema, expected_user: UserSchema):
    """
    Проверяет, что пользователь соответствует ожидаемому.

    :param actual_user: Пользователь, полученный с API.
    :param expected_user: Пользователь, ожидаемый.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual_user.id, expected_user.id, 'id')
    assert_equal(actual_user.email, expected_user.email, 'email')
    assert_equal(actual_user.last_name, expected_user.last_name, 'last_name')
    assert_equal(actual_user.first_name, expected_user.first_name, 'first_name')
    assert_equal(actual_user.middle_name, expected_user.middle_name, 'middle_name')


def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что пользователь соответствует ожидаемому.

    :param get_user_response: Пользователь, полученный с API.
    :param create_user_response: Пользователь, ожидаемый.
    :return:
    """
    assert_user(get_user_response.user, create_user_response.user)
