from enum import Enum

class AppRoute(str, Enum):
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    # Добавьте все остальные маршруты
    COURSES = "./#/courses"
    COURSES_CREATE = "./#/courses/create"