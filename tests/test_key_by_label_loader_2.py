# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from pprint import pprint

from baseblock import Enforcer
from baseblock import FileIO


from yworks_helper.core.svc import KeyByLabelLoader


def test_service():

    file_path = os.path.normpath(os.path.join(
        os.getcwd(), 'resources/testing/deepnlu-graph-nodes.json'))
    graph_results = FileIO.read_json(file_path)

    svc = KeyByLabelLoader()
    assert svc

    d_result = svc.process(d_nodes=graph_results['nodes'],
                           edges=graph_results['edges'])
    pprint(d_result)

    Enforcer.keys(d_result, 'nodes', 'edges')


def main():
    test_service()


if __name__ == "__main__":
    main()
