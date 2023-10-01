from src.providers.vacancy_provider_head_hunter import VacancyProviderHeadHunter


def test_provider_name(mocked_vacancy_provider_superjob):
    provider = VacancyProviderHeadHunter()
    assert provider.provider_name == 'Head Hunter'


def test_vacancy_provider_head_hunter_get_vacancies(mocked_vacancy_provider_head_hunter):
    provider = VacancyProviderHeadHunter()
    d = provider.get_vacancies(search_text='python')
    assert len(d.result_list) > 0
    assert d.total_results == 11615
    assert d.total_pages == 500
    assert d.page_num == 0
