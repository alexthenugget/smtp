# 📧 SMTP-клиент для отправки писем с вложениями (Yandex)

## Назначение
Этот скрипт представляет собой SMTP-клиент для отправки электронных писем через сервер Yandex с поддержкой вложений различных форматов.

## Основные компоненты системы

### 1. Основные функции

| Функция          | Назначение                                                                 |
|------------------|---------------------------------------------------------------------------|
| `send_recv`      | Отправка команд и получение ответов от SMTP-сервера                      |
| `create_msg`     | Формирование MIME-сообщения с поддержкой вложений                       |
| `send_msg`       | Основная логика взаимодействия с пользователем и отправки письма        |

### 2. Подсистемы

**Аутентификация:**
- Поддержка механизма `AUTH LOGIN`
- Автоматическое base64-кодирование учетных данных
- Обработка ответов сервера

**Формирование писем:**
- Автоматическое определение MIME-типов вложений
- Base64-кодирование файловых вложений
- Корректное оформление границ MIME-секций

**Обработка текста:**
- Чтение текста из файла или консоли
- Автоматическое экранирование строк, начинающихся с точки
- Поддержка кодировки UTF-8

### 3. Вспомогательные компоненты

| Компонент        | Назначение                                                                 |
|------------------|---------------------------------------------------------------------------|
| `exts`          | Словарь соответствий расширений файлов и MIME-типов                     |
| `dotsRe`        | Регулярное выражение для обработки специальных символов в тексте       |

## Запуск сервера

**Требования:**
- Python 3.6+
- Аккаунт Yandex с разрешенным доступом для приложений

## Конфигурация:

python
host = ('smtp.yandex.ru', 465)  # SMTP-сервер и порт
UPSTREAM_DNS = ('212.193.163.7', 53)  # Резервный DNS (не используется в текущей версии)
Поддерживаемые форматы вложений
Тип файла	Расширения	MIME-тип
Изображения	.png, .jpg, .gif	image/[тип]
Видео	.mp4	video/mp4
Аудио	.mp3	audio/mpeg

## Примеры работы

## Сценарий 1: Простое письмо

- Пользователь вводит адреса отправителя/получателя
- Указывает тему и текст
- Клиент устанавливает SSL-соединение
- Проходит аутентификацию
- Отправляет письмо

## Сценарий 2: Письмо с вложением

- Пользователь указывает путь к файлу
- Система определяет MIME-тип
- Кодирует файл в base64
- Формирует MIME-сообщение с границами
- Отправляет составное письмо
- Особенности реализации

## Безопасность:

SSL/TLS шифрование соединения
Избегание хранения паролей в открытом виде (требуется ручная настройка)

## Совместимость:

- Поддержка стандарта MIME 1.0
- Корректная обработка спецсимволов
- Автоматическое приведение к требованиям SMTP

## Производительность:

Потоковая обработка вложений
Оптимальное использование памяти при работе с большими файлами

## Настройки сервера
python
# Параметры подключения
host = ('smtp.yandex.ru', 465)  # SMTP-сервер Yandex

# Таймауты (неявные)
socket_timeout = 30  # секунд
## Для настройки необходимо:

- Заменить учетные данные в коде
- Разрешить доступ для приложений в настройках Yandex
- При необходимости изменить параметры подключения
