import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL) --> disable the log messages

'''
Logging has 5 states:

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()

they can be able and disable following the hierarchy (top to botton --> less critical to more critical)


'''

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' %(i, total))
    
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
