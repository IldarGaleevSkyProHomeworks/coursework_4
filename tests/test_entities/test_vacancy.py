from src.entities import Vacancy


def test_serialize(mocked_currency):
    vacancy = Vacancy(
        title='Vacancy 1',
        description='Vacancy description',
        url='https://example.com/vacancy/1'
    )

    assert vacancy.to_dict() == {'description': 'Vacancy description',
                                 'salary': None,
                                 'title': 'Vacancy 1',
                                 'url': 'https://example.com/vacancy/1'}


def test_deserialize(mocked_currency):
    vacancy = Vacancy.from_dict({'description': 'Vacancy description',
                                 'salary': None,
                                 'title': 'Vacancy 1',
                                 'url': 'https://example.com/vacancy/1'})

    assert vacancy.title == 'Vacancy 1'
    assert vacancy.description == 'Vacancy description'
    assert vacancy.url == 'https://example.com/vacancy/1'
    assert vacancy.salary is None
