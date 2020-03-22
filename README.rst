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

    make render

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

.. _`bottle`: https://bottlepy.org/docs/dev/
.. _`GCP`: https://en.wikipedia.org/wiki/Google_Cloud_Platform
.. _`ndb`: https://github.com/googleapis/python-ndb
.. _`SqlAlchemy`: https://github.com/sqlalchemy/sqlalchemy
.. _`chcko`: https://github.com/chcko/chcko
.. _`chcko-r`: https://github.com/chcko/chcko-r
.. _`mamchecker`: https://github.com/mamchecker/mamchecker
.. _`languages.py`: https://github.com/chcko/chcko/blob/master/chcko/chcko/languages.py
.. _`pypi`: https://pypi.org/
.. _`rst`: https://docutils.sourceforge.io/docs/user/rst/quickref.html
.. _`sphinx`: https://www.sphinx-doc.org/en/master/
.. _`latex`: https://www.latex-project.org/get/
.. _`text editor`: https://www.slant.co/topics/3418/~best-open-source-programming-text-editors


