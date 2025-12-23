import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class DataProcessor:
    def process(self, data):
        logger.debug(f"Начало обработки: {data}")
        logger.info("Обработка данных...")

        try:
            result = sum(data)
            logger.info(f"Успешно обработано. Результат: {result}")
            return result
        except Exception as e:
            logger.error(f"Ошибка: {e}")
            raise



processor = DataProcessor()
processor.process([1, 2, 3, 4, 5])
logger.warning("Это предупреждение")
logger.error("Это ошибка (для примера)")