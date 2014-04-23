# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl


def execute(next_process, handler, dependencies, **kwargs):
    def write_tmpl(template_name, values=None):
        dct = {'logged': dependencies.get('logged'),
               'username': dependencies.get('username'),
               '_login_url': dependencies.get('_login_url'),
               '_logout_url': dependencies.get('_logout_url'),
               'admin': dependencies.get('admin')}
        dct.update(values or {})
        return handler.response.write(tmpl.render(template_name, dct))

    dependencies["_write_tmpl"] = write_tmpl
    dependencies["_render"] = tmpl.render
    next_process(dependencies, **kwargs)
