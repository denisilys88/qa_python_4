from main import BooksCollector
import pytest


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        return collector

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('bookname', ['Что делать, если ваш кот хочет вас убить!', ''])
    def test_add_new_book_add_wrong_length(self, collector, bookname):
        collector.add_new_book(bookname)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('bookname', ['Что делать, если ваш кот хочет вас убить', 'A'])
    def test_add_new_book_add_edge_length(self, collector, bookname):
        collector.add_new_book(bookname)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_set_book_fantastic(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    def test_set_book_genre_set_unexisted_genre(self, collector):
        collector.add_new_book('Заводной апельсин')
        collector.set_book_genre('Заводной апельсин', 'Постмодернизм')
        assert collector.get_book_genre('Заводной апельсин') == ''

    def test_get_book_genre_get_unexisted_book(self, collector):
        assert collector.get_book_genre('Убить пересмешника') is None

    def test_get_book_genre_get_book_with_no_genre(self, collector):
        collector.add_new_book('Убить пересмешника')
        assert collector.get_book_genre('Убить пересмешника') == ''

    def test_get_books_with_specific_genre_get_by_horror(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1

    def test_get_books_genre_add_book_and_genre(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_genre() == {'Шерлок Холмс': 'Детективы'}

    def test_get_books_genre_get_empty_list(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_try_kids_books(self, collector):
        animation_name = 'Винни-Пух'
        collector.add_new_book(animation_name)
        collector.set_book_genre(animation_name, 'Мультфильмы')
        comedy_name = 'Медвежонок Паддингтон'
        collector.add_new_book(comedy_name)
        collector.set_book_genre(comedy_name, 'Комедии')

        assert collector.get_books_for_children() == [animation_name, comedy_name]

    def test_add_book_in_favorites_add_book_favourite(self, collector):
        animation_name = 'Книга джунглей'
        collector.add_new_book(animation_name)
        collector.add_book_in_favorites(animation_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_same_book_two_times(self, collector):
        fantastic_name = 'Гарри Поттер'
        collector.add_new_book(fantastic_name)
        collector.add_book_in_favorites(fantastic_name)
        fantastic_name_2 = 'Гарри Поттер'
        collector.add_new_book(fantastic_name_2)
        collector.add_book_in_favorites(fantastic_name_2)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_add_two_delete_one_favourite(self, collector):
        animation_name = 'Книга джунглей'
        collector.add_new_book(animation_name)
        collector.add_book_in_favorites(animation_name)
        fantastic_name = 'Гарри Поттер'
        collector.add_new_book(fantastic_name)
        collector.add_book_in_favorites(fantastic_name)

        collector.delete_book_from_favorites(animation_name)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_non_existed_from_favourite(self, collector):
        animation_name = 'Книга джунглей'
        collector.add_new_book(animation_name)
        collector.add_book_in_favorites(animation_name)

        collector.delete_book_from_favorites('Медвежонок Паддингтон')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_add_two_book_get_list(self, collector):
        animation_name = 'Книга джунглей'
        collector.add_new_book(animation_name)
        collector.add_book_in_favorites(animation_name)
        fantastic_name = 'Гарри Поттер'
        collector.add_new_book(fantastic_name)
        collector.add_book_in_favorites(fantastic_name)

        assert collector.get_list_of_favorites_books() == [animation_name, fantastic_name]

    def test_get_list_of_favorites_books_get_list_without_adding(self, collector):
        assert collector.get_list_of_favorites_books() == []






