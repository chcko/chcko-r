chko-r
======

A random mix of exercises and texts,
previously part of ``chcko``,
but now a separate package within the ``chcko`` namespace.

``chko-r`` is an example of content for ``chcko``.

Depends on https://github.com/chcko/chcko,
which is not automatically installed::

    pip install --user chcko

Prepare content::

    cd ~/mine/chcko-r
    # works also in sub-folders:
    doit -kd. html

    cd ~/mine/chcko-r
    doit initdb

To run content locally::

    cd ~/mine/chcko-r
    runchcko

Install content::

    cd ~/mine/chcko-r
    pip install --user .

Image files are compiled to ``/chcko-r/chcko/_images``,
and copied to ``chcko/chcko/_images`` common to all content when installing.
They need to have a globally unique name.
Use ``<author_id>_<problem_id>_xxx`` scheme, e.g ``.. texfigure:: r_dg_c1.tex``.

