#!/usr/bin/env python
# coding: utf-8

import shutil
import os


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


class LocalFileWorker(RemoteFileReader):
    TEST_DIR = 'homeworks/homework_03/test_dir'
    TMPF = 'tmpf'

    def __init__(self):
        if not os.path.isdir("./tmpf/"):
            os.mkdir("./tmpf/")

    def read_file(self, filename):
        with open(self.TEST_DIR + '/' + os.path.basename(filename) + '.tmp', 'r') as f:
            return f.read()

    def write_file(self, filename, data):
        with open(self.TMPF + '/' + os.path.basename(filename) + '.tmp', 'w') as f:
            d.writelines(data)

    def __del__(self):
        if self.TMPF in os.listdir("."):
            shutil.rmtree(self.TMPF)


class MockOrdinaryFileWorker(OrdinaryFileWorker, LocalFileWorker):

    def transfer_to_remote(self, filename):
        super().transfer_to_remote(self.TEST_DIR + '/' + filename)

    def transfer_to_local(self, filename):
        super().transfer_to_local(self.TMPF + '/' + filename)


class LLNode:
    def __init__(self, value, next_node):
        self.value ==value
        self.next_node = next_node

    def __repr__(self):
        return "value: {}; next_node: ({})".format(self.value, self.next_node)
