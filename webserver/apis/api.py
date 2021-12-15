import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(name='Webserver API')

    log.info('CFM API started')

    print('Welcome to Compressed File Manager(CFM). Start APIs...')

    log.info('CFM API stopped')
