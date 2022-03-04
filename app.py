#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
TEMPLATE: https://github.com/sharksmhi/microservice_template

Examples:
    get: http://localhost:5000/translation
    get: http://localhost:5000/translation?attribute=WINDIR
    get: http://localhost:5000/translation?attribute=PROJ&value=BLK

"""
import connexion
from translation import CodeHandler

handler = CodeHandler()


def get_info(*args, attribute=None, value=None, **kwargs):
    """Return dictionary.

    Response with code/name related information based on arguments.
    """
    return handler.get_info(
        attribute=attribute,
        value=value
    )


app = connexion.FlaskApp(
    __name__,
    specification_dir='./',
    options={'swagger_url': '/'},
)
app.add_api('openapi.yaml')

if __name__ == "__main__":
    app.run(port=5000)
