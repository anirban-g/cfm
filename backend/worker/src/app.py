import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(name='Worker APP')

    log.info('CFM WORKER started')

    print('Welcome to Compressed File Manager(CFM). Start worker...')

    log.info('CFM WORKER stopped')
