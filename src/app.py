import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(name='APP')
    log.info('CFM started')

    print('Welcome to Compressed File Manager(CFM)')

    log.info('CFM stopped')
