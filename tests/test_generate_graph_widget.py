#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from baseblock import Enforcer

from yworks_helper.core.bp import GenerateGraphWidget


def test_business_process():

    bp = GenerateGraphWidget()
    assert bp


def main():
    test_business_process()


if __name__ == "__main__":
    main()
