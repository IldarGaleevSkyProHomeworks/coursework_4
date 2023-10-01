import os.path

import pytest

from src.entities import Vacancy, Salary, Currency
from src.serializers import JsonVacancySerializer


@pytest.fixture(scope='module')
def data_list():
    return [
        Vacancy(title='Vacancy 1', salary=Salary(salary_from=Currency(value=1.0, code='CU1'))),
        Vacancy(title='Vacancy 2'),
    ]


@pytest.fixture(scope='module')
def file_name(fake_fs):
    return os.path.join(fake_fs, 'json_file_vacancy.json')


@pytest.fixture
def test_serialize(mocked_currency, data_list, file_name):
    JsonVacancySerializer.save_list_to_file(data=data_list, file_name=file_name)

    assert os.path.exists(file_name)


@pytest.mark.usefixtures('test_serialize')
def test_deserialize(mocked_currency, data_list, file_name):
    loaded_data = JsonVacancySerializer.load_list_from_file(file_name)

    assert loaded_data == data_list
