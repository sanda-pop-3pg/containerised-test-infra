#!/bin/bash
# wait-for-grid.sh

set -e

cmd="$@"

while ! curl -sSL "http://selenium-host:4444/wd/hub/status" 2>&1 \
        | jq -r '.value.ready' 2>&1 | grep "true" >/dev/null; do
    echo 'Waiting for the Selenium Host'
    sleep 1
done

>&2 echo "Selenium Host is up - executing tests"
exec $cmd