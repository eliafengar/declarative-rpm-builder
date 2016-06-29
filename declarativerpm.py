import logging
import logging.handlers
import os
import sys


class DeclarativeRpmBuilder:
    """
    A Class to Generate RPM Package using a Json file as an input
    """
    def __init__(self, settings):
        self.settings = settings

    def generate(self):
        pass


def main(settings):
    """
    The main function acting as an entry point to the App
    :param settings: the settings passed from outer application/script
    :return: None
    """
    builder = DeclarativeRpmBuilder(settings)
    builder.generate()


def configure_logger(settings):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt='%(levelname)s - %(asctime)s - %(module)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_file_path = os.path.abspath(os.path.join(settings['LOGS_FOLDER'], settings['LOG_FILE_NAME']))
    #file_handler = logging.FileHandler(os.path.join(log_file_path,
    #settings.LOG_FILE_NAME), mode='a')
    #Rotating Log FIle - 15MB each file
    file_handler = logging.handlers.RotatingFileHandler(log_file_path, mode='a', maxBytes=15728640, backupCount=10)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


if __name__ == '__main__':
    default_settings = {'LOGS_FOLDER': './logs',
                'LOG_FILE_NAME': 'declarative_rpm_builder.log'}
    configure_logger(default_settings)
    main(default_settings)