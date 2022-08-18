#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Accept Graph Data that is keyed by Label """


from baseblock import BaseObject


class KeyByLabelLoader(BaseObject):
    """ Accept Graph Data that is keyed by Label """

    def __init__(self):
        """
        Created:
            18-Aug-2022
            craigtrim@gmail.com
            *   design principles specified in
                https://github.com/craigtrim/yworks-helper/issues/1
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_nodes: dict,
                edges: list = None) -> None:
        pass
