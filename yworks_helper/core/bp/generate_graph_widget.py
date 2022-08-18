#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Generate a yWorks Graph Widget """


from baseblock import BaseObject


class GenerateGraphWidget(BaseObject):
    """ Generate a yWorks Graph Widget """

    def __init__(self):
        """
        Created:
            18-Aug-2022
            craigtrim@gmail.com
            *   design principles specified in
                https://github.com/craigtrim/yworks-helper/issues/1
        """
        BaseObject.__init__(self, __name__)

    def process(self) -> None:
        pass
