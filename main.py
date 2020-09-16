import requests
import os


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        oauth_tocken = ('OAuth ' + tocken)
        headers = {'Authorization': oauth_tocken}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers,
                                params={"path": "/test.txt"})
        address = response.json()['href']
        print(address)
        with open(self.file_path, 'rb') as f:
            resp = requests.put(address, data=f)
        return print('Файл успешно загружен.')


if __name__ == '__main__':
    tocken = input('Введите токен: ')
    fullpath = 'C:\\Users\\Лена Борисова\\PycharmProjects\\hw-9\\files\\test.txt'
    uploader = YaUploader(fullpath)
    result = uploader.upload()
