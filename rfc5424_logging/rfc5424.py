from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from rfc5424logging import Rfc5424SysLogHandler, NILVALUE

SYS_SERV = '192.168.181.43'
SYS_HOST = 'mgmt'
SYS_PORT = 514
APP_PORT = 8000
APP_NAME = 'httpd'
APP_PROC_ID = 777
INFO_PRIORITY = 6  # facility = 1, severity = 6
WARNING_PRIORITY = 5  # facility = 1, severity = 5

SYS_HANDLER = Rfc5424SysLogHandler(
    address=(SYS_SERV, SYS_PORT),
    hostname=SYS_HOST,
    appname=APP_NAME,
    procid=APP_PROC_ID,
    utc_timestamp=True)
logger = logging.getLogger('Syslog')
logger.setLevel(logging.INFO)
logger.addHandler(SYS_HANDLER)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        logger.info('msg priority <%s> \'Client %s %s %s %s\'' %
                    (INFO_PRIORITY, self.client_address[0], self.command,
                     self.path, self.request_version))


def run(server_class=HTTPServer, handler_class=Handler, port=APP_PORT):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    logger.warning('msg priority <%s> HTTPD started\n' % WARNING_PRIORITY)

    try:
        print(f"Web application \'httpd\' listens at port :{APP_PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Web application start failed: {str(e)}")
    httpd.server_close()
    print(f"Web app closed.")
    logger.warning('msg priority <%s> HTTPD stopped\n' % WARNING_PRIORITY)


if __name__ == '__main__':
    run()
