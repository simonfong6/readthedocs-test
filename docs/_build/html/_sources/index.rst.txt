.. readthedocs documentation master file, created by
   sphinx-quickstart on Mon Mar 12 00:39:28 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to readthedocs's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Installation
------------

This section borrows heavily from the readthedocs getting started guide. I am just putting this here for my own reference. The original guide can be found `here <http://docs.readthedocs.io/en/latest/getting_started.html>`_.

Install sphinx:

.. code-block:: bash

    pip install sphinx sphinx-autobuild
    
Make docs directory to keep all your doc files and required for Read The Docs.

.. code-block:: bash

    cd /path/to/project
    mkdir docs
    
Run ``sphinx-quickstart`` in the docs directory you just made.

.. code-block:: bash
    
    cd docs
    sphinx-quickstart
    
Now you will have a ``index.rst``. This will be the root of your documentation and landing page for the html. Edit this to add your own documentation according to `reStructuredText <http://www.sphinx-doc.org/en/master/rest.html>`_ syntax.

Create the html files using:

.. code-block:: bash
    
    make html
    
Your final html files can found and opened in ``_build/html/index.html``.
    

    
In order to use autodoc, in ``conf.py`` uncomment:

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('<PROJECT_PATH>'))
    
Also add autodoc and napolean (Google style docstrings) in extensions:

.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon'
    ]
    
For more information on how to write docstrings using Google style, examples are `right here <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_. More about `Google docstrings <http://www.sphinx-doc.org/en/stable/ext/napoleon.html#module-sphinx.ext.napoleon>`_.

Optional: Install Sphinx Read the docs theme by running:

.. code-block:: bash
    
    pip install sphinx_rtd_theme
    
In ``conf.py`` add:

.. code-block:: python

    html_theme = "sphinx_rtd_theme"
    
    
Autodoc
-------

An example autodoc can be found here using Google style docstrings.

.. code-block:: python

    def sum(num1,num2):
        """
        Sums two numbers.

        Args:
            num1: First number to be added. Needs to be a numerical value.
            num2: Second number to be added. Needs to be a numerical value.
             
        Returns:
            int: Sum of the two numbers.

        Raises:
            TypeError: When it is not an int or float.
        
        """
        print("Hello World!!!")
        
        if(not isinstance(int)):
            raise TypeError("Is not an int.")

        return num1 + num2


    if (__name__ == '__main__'):
        print("Hello World!!")
        
In your ``index.rst`` you can add the following, which will pull the docstring from your python files. Here my python file is callled ``main`` and I am getting the docstring for the ``sum`` function.

.. code-block:: rst
    
    The final output:

    .. autofunction:: main.sum
        
The final output:

.. autofunction:: main.sum

