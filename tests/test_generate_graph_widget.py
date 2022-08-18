#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from yfiles_jupyter_graphs import GraphWidget

from baseblock import Enforcer

from yworks_helper.core.bp import GenerateGraphWidget


def test_business_process():

    d_nodes = {
        'Jane Smith': {
            'Alpha': 220
        },
        'Joe Smith': {
            'Alpha': 45,
            'Beta': 20
        }
    }

    edges = [
        {
            'start': 'Jane Smith',
            'end': 'Joe Smith',
            'label': 'knows'
        }
    ]
    bp = GenerateGraphWidget()
    assert bp

    result = bp.process(d_nodes=d_nodes, edges=edges)
    assert type(result) == GraphWidget


def main():
    test_business_process()


if __name__ == "__main__":
    main()
