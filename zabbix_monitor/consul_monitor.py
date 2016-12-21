#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import consul
import json
import argparse
import sys


class ConsulClient:
    def __init__(self, host='127.0.0.1', port=8500):
        self.c = consul.Consul(host=host, port=port)

    def get_service_list(self):
        service_list = dict()
        service_list['data'] = [{'{#SERVICE}': service} for service in self.c.catalog.services()[1].keys()]

        print json.dumps(service_list, indent=4)

    def get_service_status(self, service):
        health = 0

        for services in self.c.health.service(service)[1]:
            for node in [check for check in services['Checks']]:
                if node.get('ServiceName') == service and node.get('Status') != 'passing':
                    health = 1

        print health


def get_ops():
    parse = argparse.ArgumentParser(description='monitor consul services.')
    parse.add_argument('--list', action='store_true', dest='list', default=False, help='Get service list.')
    parse.add_argument('-s', action='store', dest='service', type=str, help='Get service status.')

    return parse


def main():
    consul_host = '10.10.9.98'
    client = ConsulClient(host=consul_host)

    parse = get_ops()
    options = parse.parse_args()

    if options.list:
        client.get_service_list()
        sys.exit(0)
    elif options.service:
        client.get_service_status('order_api')
    else:
        parse.print_help()


if __name__ == '__main__':
    main()
