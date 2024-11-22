import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 
"""logging.INFO это тип ошибки тоесть кокая ошибка будет выводиться а format каким стиялм будеть выводиться ошибка например '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
# 2024-08-30 10:00:00,123 - INFO - User logged in successfully выводит format
# %(asctime)s: Время, когда было записано сообщение. Полезно для отслеживания временных меток событий.
# %(levelname)s: Уровень важности сообщения (например, INFO, WARNING, ERROR).
# %(message)s: Само сообщение, которое передается в лог """


class Errors:
    def log_error(self, error_message: str):
        logging.error(error_message)
        
        
    def get_error(self, type: str, e):
        if type == 'error' or type == 'errors': 
            logging.error(e)
        
    
    def database_error(self, error_message: str = None):
        if not error_message:
            try:
                raise ValueError('Database is unavailable, check connection')
            except ValueError as e:
                self.get_error('error', e)
                
        return 'Hello world'
            
    
errors: Errors = Errors()