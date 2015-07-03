chimera-jmismart232 plugin
==========================

A chimera_ plugin for `JMI Smart 232`_ focusers.

Usage
-----

Install chimera_ on your computer, and then, this package. Edit the configuration file adding
the JMI Smart 232 configuration as on the example below.

Installation
------------

Besides chimera_, ``chimera-jmismart232`` depends only of pyserial_.

::

    pip install -U git+https://github.com/astroufsc/chimera-jmismart232.git


Configuration Example
---------------------

* `JMI Smart 232`_ focuser

::

    focuser:
      name: jmismart
      type: JMIsmart232
      device: COM3          # /dev/ttyS?? on linux


Tested Hardware
---------------

This plugin was tested on these hardware:

* `JMI Smart 232`_ focuser


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-jmismart232/

.. _chimera: https://www.github.com/astroufsc/chimera/
.. _pyserial: http://pyserial.sourceforge.net/
.. _JMI Smart 232: http://www.jimsmobile.com/
.. _LNA: http://www.lna.br/
.. _MEADE LX200: http://www.meade.com/products/telescopes/lx200.html
.. _Optec TCF-S: http://www.optecinc.com/astronomy/catalog/tcf/tcf-s.htm
