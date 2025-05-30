import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


url = "https://astanahub.com/ru/service/techpark/"
fake_user = UserAgent()
headers = {"User-Agent": fake_user.random}


def hub_parser() -> list:
    """Parses https://astanahub.com/ru/service/techpark/ webpage ONLY"""
    
    participants = []

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    rows = soup.find('table', class_='table').find('tbody').find_all('tr')
    if not rows:
        print("Таблица с участниками международного технологического парка 'Астана Хаб'  не найдена.")
        return

    for row in rows[:10]:
        tds = row.find_all('td')

        participant = {
            'id': tds[0].text.strip(),
            'registration_date': tds[1].text.strip(),
            'valid_until': tds[2].text.strip(),
            'company_bin': tds[3].text.strip(),
            'status': tds[4].text.strip(),
            'company_name': tds[5].text.strip()
        }

        participants.append(participant)

    return participants


if __name__ == "__main__":
    hub_parser()