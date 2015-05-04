barf

echo "192.168.7.2" > ./ansible_hosts
export ANSIBLE_HOSTS=./ansible_hosts

sshfs thorsten@192.168.7.2:Barfly/ ./Beaglemount/  -oauto_cache,reconnect,defer_permissions,noappledouble,negative_vncache,volname=myVolName
