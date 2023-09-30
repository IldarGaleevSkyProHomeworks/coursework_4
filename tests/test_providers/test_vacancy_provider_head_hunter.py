from src.providers.vacancy_provider_head_hunter import VacancyProviderHeadHunter


def test_vacancy_provider_head_hunter_get_vacancies(mocked_vacancy_provider_head_hunter):
    provider = VacancyProviderHeadHunter()
    d = provider.get_vacancies(search_text='python')
    assert len(d) > 0
