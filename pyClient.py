import sys
import glob
sys.path.append('../gen-py')  # Changed
sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from mytest import Tester  # Changed
from mytest.ttypes import *  # Changed

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Tester.Client(protocol)
    transport.open()

    sum_ = client.add(3, 4)
    print('3 + 4 = %d' % sum_)
    # Changed
    str_ = client.merge('Hello ', 'Python')
    print('Hello + Python = %s' % str_)

    transport.close()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)