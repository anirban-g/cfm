import logging
from time import sleep

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(name='Orchestrator APP')

    log.info('CFM Orchestrator started')

    print('Welcome to Compressed File Manager(CFM). Start Orchestrator...')
    log.info(f'Going to sleep for 5 minutes...')
    sleep(300.0)

    log.info('CFM Orchestrator stopped')
