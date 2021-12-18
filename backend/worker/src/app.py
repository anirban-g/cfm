from time import sleep

import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(name='Worker APP')

    log.info('CFM WORKER started')

    print('Welcome to Compressed File Manager(CFM). Start worker...')
    log.info(f'Going to sleep for 5 minutes...')
    sleep(300.0)

    log.info('CFM WORKER stopped')
