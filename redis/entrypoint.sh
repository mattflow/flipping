#!/bin/sh
echo "user ${REDIS_USERNAME:-default} on >${REDIS_PASSWORD:-changeme} allkeys allchannels allcommands" > /tmp/users.acl
exec redis-server --aclfile /tmp/users.acl