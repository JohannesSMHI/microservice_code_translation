
Code translator - microservice
==============================

🧰 About - Usage
-----------------

Developed by Shd at SMHI.

- Python based service using Flask
- Get translation for codes/names used at the Swedish NODC
- `Microservice Template <https://github.com/shark-microservices/microservice_template>`_
- Download the `code list <http://smhi.se/oceanografi/oce_info_data/shark_web/downloads/codelist_SMHI.xlsx>`_


💻 Installation - Getting started
----------------------------------

**Create a virtual environment for your project with venv:**

.. code-block:: bash

    python -m venv venv

Activate the virtual environment:

.. code-block:: bash

    source ./venv/bin/activate

Install requirements with pip:

.. code-block:: bash

    pip install -r requirements.txt

--------------------------------------------------------------------------------

**Alternative with conda:**

.. code-block:: bash

    conda env create --file environment.yaml

Activate environment:

.. code-block:: bash

    conda activate py38
