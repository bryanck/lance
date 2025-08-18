#!/bin/bash

desc=$(metatron curl -provideE2eToken -a lancerestcatalog -X POST -H 'content-type: application/json' https://lancerestcatalog.cluster.us-east-1.prod.cloud.netflix.net:7004/v1/table/bkeller.foobar2/describe -d '{"id":["bkeller", "foobar2"]}')
access_key_id=$(echo $desc | jq -r .storage_options.access_key_id)
secret_access_key=$(echo $desc | jq -r .storage_options.secret_access_key)
session_token=$(echo $desc | jq -r .storage_options.session_token)

echo $access_key_id > creds
echo $secret_access_key >> creds
echo $session_token >> creds

