import pytest
from datetime import datetime, date
import logging

logger=logging.getLogger(__name__)


@pytest.fixture()
def input_ide():
    return '1TIByNOR1RMRm5KQE72iC-h5Z-nPYhtOI'


def pytest_assertrepr_compare(op, left, right):
  
    logger.error('Comparing Foo instances:','   vals: %s != %s\n' % (left, right))
    return ['Comparing Foo instances:','   vals: %s != %s\n' % (left, right)]


def pytest_configure(config):
    '''Creates a log file if log_file is not mentioned in the .ini file'''
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H_%M_%S')
        #This will create a new log filw with current datestamp
        config.option.log_file = 'pytest.log'
