import requests
from bs4 import BeautifulSoup


def translate_yandex(text, lang_from, lang_to):
    url = "https://translate.yandex.ru/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    params = {
        'lang': f'{lang_from}-{lang_to}',
        'text': text
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Здесь необходимо найти правильный элемент, содержащий перевод
        translation = soup.find('div', class_='translation-container').get_text(strip=True)
        return translation
    else:
        return None


translated_text = translate_yandex("Привет, как дела?", "ru", "en")
print(translated_text)
