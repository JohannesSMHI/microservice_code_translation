#!/usr/bin/env python3
# Copyright (c) 2020 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2021-11-15 17:52

@author: johannes
"""
import os
import sys
import pandas as pd

PYTHON_VERSION = int(f'{sys.version_info.major}{sys.version_info.minor}')
RESOURCES = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'resources'
)


class CodeHandler(dict):
    """Class to map codes.

    Mapping codes against its relative translations swedish/english/short names.

    Initialize: ch = CodeHandler()
    Call:
        - ch.map_get('WAVES', '6')
        - ch.map_get('WAVES', 'estimated wave height: 4 - 6m')
    Out: {
        'Index': 1281,
        'field': 'WAVES',
        'code': '6',
        'sv': 'Uppskattad våghöjd: 4 - 6m. Sjön tornar upp sig och bryter,
               skummet ordnar upp sig i strimmor i vindens riktning.',
        'en': 'estimated wave height: 4 - 6m'
    }
    """

    mapper = {
        'ALABO': 'LABO',
        'RLABO': 'LABO',
        'SLABO': 'LABO',
        'ORDERER': 'LABO',
        'CURDIR': 'WINDIR',
        'REFSK_SMP': 'REFSK',
        'REFSK_ANA': 'REFSK',
        'ADD_SMP': 'DTYPE',
    }

    def __init__(self, **kwargs):
        """Initialize and set dict."""
        super().__init__(**kwargs)

        cl = pd.read_excel(
            os.path.join(RESOURCES, 'codelist_SMHI.xlsx'),
            sheet_name="codelist_SMHI",
            header=1,
            dtype=str,
            keep_default_na=False,
            engine=None if PYTHON_VERSION >= 37 else 'openpyxl'
        )
        cl = cl.rename(
            {
                'Data_field': 'field',
                'Code': 'code',
                'Beskrivning/Svensk översättning': 'sv',
                'Description/English translate': 'en'
            },
            axis=1
        )

        for attr in cl['field'].unique():
            boolean = cl['field'] == attr
            attr_dict = {}
            for row in cl[boolean].itertuples():
                as_dict = row._asdict()
                for key, value in as_dict.items():
                    if key not in ('Index', 'field'):
                        attr_dict.setdefault(value, as_dict)
            self.setdefault(attr, attr_dict)

    def map_get(self, attribute, value):
        """Return value for a given attribute and a value to translate.

        The given value can be either "code", "sv" or "en",
        they will all return the same dictionary.
        """
        if attribute.startswith('Q_'):
            attribute = 'QFLAG'
        attribute = self.mapper.get(attribute, attribute)
        if attribute not in self:
            return None
        else:
            return self[attribute].get(value)

    def get_info(self, attribute=None, value=None):
        """Return info based on the given attribute and/or value."""
        if attribute and value:
            return self.map_get(attribute, value)
        elif attribute:
            return self.get(self.mapper.get(attribute, attribute))
        elif value:
            return (
                'Missing attribute, got attribute={}; value={}'.format(
                    attribute,
                    value
                ),
                404
            )
        else:
            return {'available-attributes': list(self.keys())}


if __name__ == "__main__":
    ch = CodeHandler()
