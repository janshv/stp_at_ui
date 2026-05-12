from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.fixture()
def clear_books_db():
    print('\n [FIXTURE] delete all data from books db')

@pytest.fixture()
def fill_books_db():
    print('\n [FIXTURE] fill books db with data')


@pytest.mark.usefixtures('fill_books_db')
def test_read_all_books_in_lib():
    print('\n Reading all books')

@pytest.mark.usefixtures('clear_books_db', 'fill_books_db')
class TestLibrary:

    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...

