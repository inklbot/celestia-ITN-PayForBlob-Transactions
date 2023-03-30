#!/bin/bash

# Send a POST request and save the response in a variable
response=$(curl -s -X POST -d '{"namespace_id": "0c204d39600fddd3",
  "data": "f1f20ca8007e910a3bf8b2e61da0f26bca07ef78717a6ea54165f5",
  "gas_limit": 80000, "fee": 2000}' http://localhost:26659/submit_pfb)

# Extract the height and txhash values from the response
height=$(echo $response | jq -r '.height')
txhash=$(echo $response | jq -r '.txhash')

# Send a GET request to retrieve data using the extracted height value
data=$(curl -s -X GET http://localhost:26659/namespaced_shares/0c204d39600fddd3/height/$height)

# Print the results
echo ""
echo "Height: $height"
echo "Transaction Hash: $txhash"
echo "https://testnet.mintscan.io/celestia-incentivized-testnet/txs/$txhash"
echo ""
