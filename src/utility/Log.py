import logging


class Log:
    logLocation = ".\\logs"

    @staticmethod
    def boot_log():
        logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
