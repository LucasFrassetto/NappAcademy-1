import http.client
from ftplib import FTP


class SimpleFactory:
    @staticmethod
    def build_connection(protocol):
        if protocol == 'http':
            return http.client.HTTPConnection('python.org')
        elif protocol == 'ftp':
            ftp = FTP('ftp1.at.proftpd.org')
            ftp.login()
            return ftp
        else:
            raise RuntimeError('Unknown protocol')


if __name__ == '__main__':
    protocols = ['http', 'ftp', 'https']
    for protocol_name in protocols:
        print('Protocolo: ' + protocol_name + '\n\n')
        protocol = SimpleFactory.build_connection(protocol_name)
        protocol.connect()
        print(protocol.sock)
        protocol.close()
