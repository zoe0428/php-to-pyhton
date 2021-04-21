import glob
import sys
sys.path.append('../gen-py')  # Changed
sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from mytest import Tester  # Changed
from mytest.ttypes import *  # Changed

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

# Changed
class TesterHandler:
    def __init__(self):
        self.log = {}

    def add(self, num1, num2):
        print('add(%d, %d) is called' % (num1, num2))
        return num1 + num2

    def merge(self, str1, str2):
        print('merge(%s, %s) is called' % (str1, str2))
        return str1 + str2

if __name__ == '__main__':
    handler = TesterHandler()  # Changed
    processor = Tester.Processor(handler)  # Changed
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')