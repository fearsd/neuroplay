# Как запустить?

1. Скачать репозиторий
2. Перейти в корневую папку проекта в терминале
3. Сделать виртуальное окружение: `python3 -m venv venv`
4. Установить зависимости: `pip install -r requirements.txt`
5. Запустить проект: `python main.py`

Проект запустится по адресу http://localhost:5555

# Для деплоя
1. Установить зависимости через conda
`conda create -n venv python=3.9`
`conda activate venv`
`conda install torch`
`conda install pytorch torchvision torchaudio cpuonly -c pytorch`
`conda install transformers`
`conda install gunicorn`

2. Создать neuroplay.service (пример есть в репозитории)
`sudo nano /etc/systemd/system/neuroplay.service`
3. Запустить по команде и открыть порт. Проект будет доступен по адресу vps_ip_address:5555
`sudo systemctl start neuroplay`
`sudo systemctl enable neuroplay`
