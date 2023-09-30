from src.providers.vacancy_provider_superjob import VacancyProviderSuperjob


def test_provider_name(mocked_vacancy_provider_superjob):
    provider = VacancyProviderSuperjob()
    assert provider.provider_name == 'Superjob'


def test_vacancy_provider_superjob_get_vacancies(mocked_vacancy_provider_superjob):
    provider = VacancyProviderSuperjob()
    provider.API_KEY = 'FAKE_KEY'
    d = provider.get_vacancies(search_text='python')
    assert len(d.result_list) > 0
    assert d.total_results == 879
    assert d.total_pages == 44
    assert d.page_num == 0


def test_vacancy_provider_superjob_get_vacancies_without_API_KEY(mocked_vacancy_provider_superjob):
    provider = VacancyProviderSuperjob()
    provider.API_KEY = None
    d = provider.get_vacancies()
    assert d.result_list == []
