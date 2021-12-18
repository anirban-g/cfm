import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(name='Orchestrator APP')

    log.info('CFM Orchestrator started')

    print('Welcome to Compressed File Manager(CFM). Start Orchestrator...')

    log.info('CFM Orchestrator stopped')
