#!/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 et

# syncrepl_client exceptions code.
#
# Refer to the AUTHORS file for copyright statements.
#
# This file is made available under the terms of the BSD 3-Clause License,
# the text of which may be found in the file `LICENSE.md` that was included
# with this distribution, and also at
# https://github.com/akkornel/syncrepl/blob/master/LICENSE.md 
#
# The Python docstrings contained in this file are also made available under the terms
# of the Creative Commons Attribution-ShareAlike 4.0 International Public License,
# the text of which may be found in the file `LICENSE_others.md` that was included
# with this distribution, and also at
# https://github.com/akkornel/syncrepl/blob/master/LICENSE_others.md
#


class VersionError(Exception):
    """Database is too new.

    This exception is thrown when attempting to use a database that was either
    created with a newer version of syncrepl_client, or was created in a newer
    version of Python.

    Class includes the following attributes:

    * `component`: Either "python" or "syncrepl_client".

    * `their_version`: A tuple.

    * `our_version`: Another tuple.
    """
    def __init__(self, which, ours, db):
        self.our_version = ours
        self.their_version = db
        self.component = which

    def __str__(self):
        return (  '%s is version %s, but we are %s'
                % (self.component, self.their_version, self.our_version))


class VersionJumpError(VersionError):
    def __str__(self):
        return (  'Can not jump from Python %d to Python %d'
                % (self.their_version, self.our_version))


class ClosedError(Exception):
    """Action performed on an unbound instance.

    This exception is thrown when a call is made to an instance which has been
    unbound.

    If you wish to reconnect to the server, you must use a new instance.
    """
    pass


class LDAPUrlError(Exception):
    """Generic LDAP URL-related exception.

    All of the exceptions related to LDAP URLs are subclasses of this
    exception.
    """
    pass


class LDAPUrlConflict(LDAPUrlError):
    """Thrown when a URL conflicts with an existing URL.

    This exception is thrown when a data store already has a URL, and the
    client provided a new LDAP URL that conflicts.

    The following attributes should be checked:

    * The search base DN.

    * The search scope.

    * The search filter.

    * The list of attributes to return.

    If any of the above attributes conflict, this exception is thrown.

    Attributes:

        current_url -- An :class:`~ldapurl.LDAPUrl` object; the current URL.

        new_url -- An :class:`~ldapurl.LDAPUrl` object; the new, conflicting URL.
    """

    def __init__(self, current_url, new_url):
        self.current_url = current_url
        self.new_url = new_url


class LDAPUrlParseError(LDAPUrlError):
    """Thrown when an LDAP URL can not be parsed.

    This exception is thrown when an LDAP URL string is provided, but that
    string can not be parsed.

    Attributes:

        url -- The URL string provided by the client.
    """

    def __init__(self, url):
        self.url = url


class DBError(Exception):
    pass


class DBConsistencyWarning(Warning):
    pass


class DBSchemaError(DBError):
    pass


class SchemaVersionError(DBError):
    pass


class DBSettingError(DBError):
    pass
