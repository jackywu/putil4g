#!/usr/bin/env bash
# vim: fileencoding=utf-8 autoindent tabstop=2 shiftwidth=2 expandtab softtabstop=2 filetype=sh

cd $(dirname $0)

python3 -m tests.runtests "$@"
