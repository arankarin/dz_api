

def dictionary_check_from_response(response):
    """Функция проверки ключчей из ответа"""
    lict_1 = [
        "id",
        "name",
        "brewery_type",
        "street",
        "address_2",
        "address_3",
        "city",
        "state",
        "county_province",
        "postal_code",
        "country",
        "longitude",
        "latitude",
        "phone",
        "website_url",
        "updated_at",
        "created_at"
    ]
    if isinstance(response, dict):
        for i in lict_1:
            try:
                response.get(i)
            except KeyError:
                return False
        return True
    else:
        for i in lict_1:
            for res_dict in response:
                try:
                    res_dict[i]
                except KeyError:
                    return False
            return True
