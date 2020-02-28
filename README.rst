chko-r
======

A random mix of exercises and texts,
previously part of ``chcko``,
but now a separate package within the ``chcko`` namespace.

``chko-r`` is an example of content for ``chcko``.

Depends on https://github.com/chcko/chcko,
which is not automatically installed::

    pip install --user chcko

There is no need to install ``chcko``, if ``chcko`` is parallel to ``chcko-r``.

Prepare content::

    make render

To run content locally (chcko needs to be installed)::

    cd chcko-r
    runchcko

Install content::

    cd chcko-r
    pip install --user .

Image files are compiled to ``/chcko-r/chcko/_images``,
and copied to ``chcko/chcko/_images`` common to all content when installing.
They need to have a globally unique name.
Use ``<author_id>_<problem_id>_xxx`` scheme, e.g ``.. texfigure:: r_dg_c1.tex``.

