from src.providers.vacancy_provider_superjob import VacancyProviderSuperjob


def test_vacancy_provider_superjob_get_vacancies(mocked_vacancy_provider_superjob):
    provider = VacancyProviderSuperjob()
    d = provider.get_vacancies(search_text='python')
    assert len(d) > 0


def test_vacancy_provider_superjob_get_vacancies_without_API_KEY(mocked_vacancy_provider_superjob):
    provider = VacancyProviderSuperjob()
    provider.API_KEY = None
    d = provider.get_vacancies()
    assert d == []
