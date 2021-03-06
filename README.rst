chko-r
======

`chko-r`_ is an example content package and test data for `chcko`_.
`chko-r`_ is a random mix of problems and texts.

A live version is available at:

    https://chcko.eu

This python package depends on the `chcko`_ python package,
which is not automatically installed,
because on gcloud `chcko`_ is *uploaded*, not installed.
Therefore locally install with::

    pip install --user chcko
    pip install --user chcko-r

There is no need to install,
if `chcko`_ is parallel to `chcko-r`_.

A content package can add additional dependencies.
This ``chcko-r`` depends on
`schemdraw <https://pypi.org/project/SchemDraw/>`__
`pint <https://pypi.org/project/Pint/>`__.
To install the dependencies without installing ``chcko-r``,
use ``pip install -r requirements.txt``.

Prepare content::

    make html

To run content locally with `chcko`_ installed::

    cd chcko-r
    runchcko

Install content::

    cd chcko-r
    pip install --user .

Image files are compiled to ``/chcko-r/chcko/_images``,
and copied to ``chcko/chcko/_images`` common to all `chcko`_ content when installing.
Image files need to have globally unique names across all ``chcko-<author_id>`` packages.
Use ``<author_id>_<problem_id>_xxx`` scheme,
e.g ``.. texfigure:: r_dg_c1.tex``.

Images can also be generated on the fly.
Examples:
`r.a3 <https://github.com/chcko/chcko-r/blob/master/chcko/r/a3/circuit.html>`__
`r.a4 <https://github.com/chcko/chcko-r/blob/master/chcko/r/a4/circuit.html>`__.

.. _`chcko`: https://github.com/chcko/chcko
.. _`chcko-r`: https://github.com/chcko/chcko-r


