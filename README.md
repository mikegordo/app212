Django + DrangoRestFramework example with token authentication

`GET` request:

    curl -s -H "Authorization: Token 0admin0abcd0192837465abcd657483929abcd44" \
    "127.0.0.1:8000/v1/tick/1" | jq .

`POST` request:

    curl -X POST -H "Authorization: Token 0admin0abcd0192837465abcd657483929abcd44" \
    -H "Content-Type: application/json" \
    -d '{"payload":{"foo":"bar"}}' "127.0.0.1:8000/v1/tick" | jq .

