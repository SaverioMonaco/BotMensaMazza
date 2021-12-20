#!/bin/sh

# On Nassuz perl is under /opt/bin, which is not in PATH
PATH="$PATH:/opt/bin/"

# Start perl package if not already started
if ! /usr/bin/env which perl; then
    /share/CACHEDEV1_DATA/.qpkg/Perl/Perl.sh start
fi

exec /usr/bin/env perl $@
