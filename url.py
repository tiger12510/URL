import requests


class YaUploader:

    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

        file_name = file_path.split('/', )[-1]

        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

        param = {"path": f"Загрузки/{file_name}", "overwrite": "true"}

        _response = requests.get(upload_url, headers=headers, params=param).json()

        hiref = _response.get("hiref", "")

        responce = requests.put(hiref, data=open(file_path, 'rb'))

        responce.raise_for_status()

        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    path_to_file = 'Users\sanec\Desktop\tasks-math-4-11-sch-msk-20-21.pdf'
    token = ' '

    uploader = YaUploader(token)

    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)