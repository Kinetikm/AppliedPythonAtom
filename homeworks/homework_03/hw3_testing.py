#!/usr/bin/env python
# coding: utf-8
import os
import shutil


class Requester:

    def get(self, host, port, filename):
        return "Fail"

    def post(self, host, port, filename, data):
        return False


class RemoteFileReader(Requester):

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def read_file(self, filename):
        return super().get(self._host, self._port, filename)

    def write_file(self, filename, data):
        return super().post(self._host, self._port, filename, data)


class OrdinaryFileWorker(RemoteFileReader):

    def transfer_to_remote(self, filename):
        with open(filename, "r") as f:
            super().write_file(filename, f.readlines())

    def transfer_to_local(self, filename):
        with open(filename, "w") as f:
            f.write(super().read_file(filename))


class TrueClass(RemoteFileReader):

    def __init__(self):
        # create dir
        if not os.path.exists('tmpf'):
            os.makedirs('tmpf')

    def __del__(self):
        if 'tmpf' in os.listdir('.'):
            shutil.rmtree('tmpf')

    def read_file(self, filename):
        path = 'homeworks/homework_03/test_dir/'
        filename = path + os.path.basename(filename)
        with open(filename + '.tmp', 'r') as f:
            return f.read()

    def write_file(self, filename, data):
        filename = 'tmpf/' + \
                   os.path.basename(filename)
        with open(filename + '.tmp', 'w') as f:
            return f.writelines(data)


class MockOrdinaryFileWorker(OrdinaryFileWorker, TrueClass):

    def __init__(self):
        raise NotImplementedError

    def transfer_to_remote(self, filename):
        super().transfer_to_remote('homeworks/homework_03/test_dir/' + filename)

    def transfer_to_local(self, filename):
        super().transfer_to_local('tmpf/' + filename)


class LLNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "value: {}; next_node: ({})".format(self.value, self.next_node)
