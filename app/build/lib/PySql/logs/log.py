import logging
from typing import Optional


# logging.basicConfig(level=logging.INFO, format=format) 
"""logging.INFO это тип ошибки тоесть кокая ошибка будет выводиться а format каким стиялм будеть выводиться ошибка например '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
# 2024-08-30 10:00:00,123 - INFO - User logged in successfully выводит format
# %(asctime)s: Время, когда было записано сообщение. Полезно для отслеживания временных меток событий.
# %(levelname)s: Уровень важности сообщения (например, INFO, WARNING, ERROR).
# %(message)s: Само сообщение, которое передается в лог """


LOGGING_METHOD = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')

class ErrorLogger:
    def __init__(self, name: str = 'application_logger', level: int = logging.INFO) -> None:
        # Получаем или создаем логгер с указанным именем.
        # Если логгер с таким именем уже существует, он будет возвращен, иначе создается новый.
        self.logger = logging.getLogger(name)
        
        # Устанавливаем уровень логирования для логгера.
        # Сообщения ниже этого уровня игнорируются (например, INFO, DEBUG, WARNING и т.д.).
        # у каждого лвл логирование идет приоритет 1 DEBUG 2 INFO 3 WARNING 4 ERROR 5 CRITICAL
        self.logger.setLevel(level)
        
        # Определяем формат вывода логов. 
        # Включаем такие параметры, как время записи, уровень логирования, файл и номер строки, откуда идет лог, и само сообщение.
        format = 'Time: %(asctime)s - Level: %(levelname)s - File: %(filename)s - Line: %(lineno)d - Message: %(message)s'
        
        # Создаем объект форматтера, который будет отвечать за то, как сообщения будут отображаться согласно определенному выше формату.
        formatter = logging.Formatter(format)
        
        try:
            # Создаем обработчик для отправки сообщений в поток (в данном случае - консоль).
            console_handler = logging.StreamHandler() #StreamHandler используется для отправки сообщений журнала в поток, например, на консоль (стандартный вывод) или в файл.
            
            # Проверяем, успешно ли создан обработчик.
            # Если по какой-то причине он не создан, выбрасываем исключение (здесь эта проверка избыточна, так как создание всегда проходит успешно).
            if not console_handler:
                raise ValueError('Not Found console_handler')
            
            # Устанавливаем созданный форматтер для обработчика.
            # Это означает, что все сообщения, проходящие через console_handler, будут форматированы в соответствии с заданным форматом.
            console_handler.setFormatter(formatter) #setFormatter настраивает форматирование сообщений журнала, которые обрабатывает обработчик
        except ValueError as ve:
            # Ловим исключение и передаем его дальше, если возникла проблема с созданием обработчика.
            raise ve
        
        if not self.logger.handlers:
            # Проверяем, есть ли уже обработчики у логгера.
            # Если обработчиков нет, добавляем наш обработчик, который будет выводить логи в консоль.
            # Эта проверка предотвращает дублирование обработчиков, чтобы один и тот же обработчик не добавлялся несколько раз.
            self.logger.addHandler(
                console_handler
            )
            
    def is_valid(self, type):
        if not type or (
            not isinstance(type, str) 
            or 
            type.upper() not in LOGGING_METHOD):
            return False
        return True
            

    def _table_exists(self, type, error_message):
        if self.is_valid(type=type):
            self.logger.error(error_message)
    
    def _log_error(self, type, error_message):
        if self.is_valid(type=type):
            self.logger.error(error_message)
            
    def _log_info(self, type, info_message):
        if self.is_valid(type=type):
            self.logger.info(info_message)
            
            
            
class Errors(ErrorLogger):
    def __init__(self) -> None:
        super().__init__(level=logging.ERROR)
        
    def execute_query_log(self, info_message):
        self._log_info('info', info_message)
        
    def table_exists(self, error_message):
        self._table_exists('error', error_message)
    
    def connect_error(self, error_message: str):
        self._log_error('error', error_message)
        
    def database_error(self, error_message: str = None):
        self._log_error(error_message, 'Database is unavailable, check connection')
            
 
errors = Errors()