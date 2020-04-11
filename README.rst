chko-r
======

`chko-r`_ is an example content package for `chcko`_,
a random mix of problems and texts,
availabe at

    https://chcko.eu


This python package depends on the `chcko`_ python package,
which is not automatically installed,
because on gcloud `chcko`_ is uploaded and not installed.
Therefore locally install with::

    pip install --user chcko
    pip install --user chcko-r

There is no need to install `chcko`_,
if `chcko`_ is parallel to `chcko-r`_.

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
Image files need to have globally unique names across ``chcko-<author_id>`` packages.
Use ``<author_id>_<problem_id>_xxx`` scheme,
e.g ``.. texfigure:: r_dg_c1.tex``.

.. _`chcko`: https://github.com/chcko/chcko
.. _`chcko-r`: https://github.com/chcko/chcko-r


