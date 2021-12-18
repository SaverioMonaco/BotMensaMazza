#!/bin/sh

# On Nassuz perl is under /opt/bin, which is not in PATH
exec /usr/bin/env PATH="$PATH:/opt/bin" perl $@ 
