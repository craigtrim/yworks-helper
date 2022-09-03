from yworks_helper.core.svc import KeyByLabelLoader
from baseblock import Enforcer
from pprint import pprint
{
    "1214eded_1f2c_11ed_bf52_4c1d96716627": {
        "end": "1214edec_1f2c_11ed_82a7_4c1d96716627",
        "label": "knows",
        "start": "1214edeb_1f2c_11ed_a2f2_4c1d96716627"
    }
}  # !/usr/bin/env python
# -*- coding: UTF-8 -*-


def test_service():

    d = {
        "john smith": {
            "alpha": 22
        },
        "jane smith": {
            "alpha": 233,
            "beta": 400
        }
    }

    e = [
        {
            'start': 'john smith',
            'end': 'jane smith',
            'label': 'knows'
        }
    ]

    svc = KeyByLabelLoader()
    assert svc

    d_result = svc.process(d, e)
    pprint(d_result)

    Enforcer.keys(d_result, 'nodes', 'edges')

    # can't assert absolute structure because IDs are dynamic

    # Nodes:
    # [
    #     {
    #         "id": "75869532_1f2a_11ed_b851_4c1d96716627",
    #         "properties": {
    #             "alpha": 22,
    #             "label": "john smith"
    #         }
    #     },
    #     {
    #         "id": "75869533_1f2a_11ed_a34a_4c1d96716627",
    #         "properties": {
    #             "alpha": 233,
    #             "beta": 400,
    #             "label": "jane smith"
    #         }
    #     }
    # ]

    # Edges:
    # {
    #     "1214eded_1f2c_11ed_bf52_4c1d96716627": {
    #         "end": "1214edec_1f2c_11ed_82a7_4c1d96716627",
    #         "label": "knows",
    #         "start": "1214edeb_1f2c_11ed_a2f2_4c1d96716627"
    #     }
    # }


def main():
    test_service()


if __name__ == "__main__":
    main()
