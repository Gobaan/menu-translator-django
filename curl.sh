curl localhost:8000/graphql \
  -F operations='{ "query": "mutation($files: [Upload!]!) { imageMutation(picture: $files[0]) { id } }", "variables": { "files": [null, null] } }' \
  -F map='{ "0": ["variables.files.0"], "1": ["variables.files.1"] }' \
  -F 0=test.txt \
  -F 1=test.txt \
  -v -c cookies.txt -b cookies.txt
