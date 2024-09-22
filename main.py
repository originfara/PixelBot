import requests
import time
import threading

# URL и заголовки для POST-запроса
post_url = "https://notpx.app/api/v1/repaint/start"
post_headers = {
    "Authorization": "initData user=%7B%22id%22%3A608927977%2C%22first_name%22%3A%22TOF%F0%9F%90%B8%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22thetofix%22%2C%22language_code%22%3A%22ru%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=1621039160858601012&chat_type=sender&auth_date=1726987761&hash=5337b4b0eed24462ede2997a783b57acae199282cb17ab6d03432d6100254ef2",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
}
post_data = {
    "pixelId": 392524,
    "newColor": "#51E9F4"
}

# URL и заголовки для GET-запроса
get_url = "https://notpx.app/api/v1/mining/claim"
get_headers = {
    "Authorization": "initData user=%7B%22id%22%3A608927977%2C%22first_name%22%3A%22TOF%F0%9F%90%B8%22%2C%22last_name%22%3A%22%22%2C%22username%22%3A%22thetofix%22%2C%22language_code%22%3A%22ru%22%2C%22allows_write_to_pm%22%3Atrue%7D&chat_instance=1621039160858601012&chat_type=sender&auth_date=1726987761&hash=5337b4b0eed24462ede2997a783b57acae199282cb17ab6d03432d6100254ef2",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.146 Mobile Safari/537.36"
}

# Функция для POST-запроса
def post_request():
    while True:
        response = requests.post(post_url, headers=post_headers, json=post_data)
        if response.status_code == 200:
            print("POST-запрос успешен")
        else:
            print(f"Ошибка POST-запроса: {response.status_code}")
        time.sleep(200)  # Пауза 200 секунд

# Функция для GET-запроса
def get_request():
    while True:
        response = requests.get(get_url, headers=get_headers)
        if response.status_code == 200:
            print("GET-запрос успешен")
        else:
            print(f"Ошибка GET-запроса: {response.status_code}")
        time.sleep(3600)  # Пауза 1 час (3600 секунд)

# Запуск потоков
post_thread = threading.Thread(target=post_request)
get_thread = threading.Thread(target=get_request)

post_thread.start()
get_thread.start()

post_thread.join()
get_thread.join()
