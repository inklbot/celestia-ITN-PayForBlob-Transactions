#!/bin/bash

# Generate a random namespace ID
nID=$(head -c 8 /dev/urandom | xxd -p)

# Generate a random hex-encoded message
hexdata=$(head -c 27 /dev/urandom | xxd -p)

echo "Random hex-encoded namespace ID: $nID"
echo "Random hex-encoded data: $hexdata"
echo ""

# Send a POST request and save the response in a variable
echo "Sending a POST request..."
response=$(curl -s -X POST -d '{"namespace_id": "'"$nID"'", "data": "'"$hexdata"'", "gas_limit": 80000, "fee": 2000}' http://localhost:26659/submit_pfb)

# Extract the height and txhash values from the response
echo $response | jq .
echo ""

height=$(echo $response | jq -r '.height')
txhash=$(echo $response | jq -r '.txhash')

# Send a GET request to retrieve data using the extracted height value
echo "Retrieving data based on POST results..."
data=$(curl -s -X GET http://localhost:26659/namespaced_shares/"$nID"/height/"$height")

echo $data | jq .

# Print the results and save them to the log file
{
    echo "----------------------------------------------------------------------"
    echo "Date and Time: $(date +"%Y-%m-%d %H:%M:%S")"
    echo ""
    echo "Namespace ID: $nID"
    echo "Data: $hexdata"
    echo ""
    echo "Height: $height"
    echo "Transaction Hash: $txhash"
    echo "https://testnet.mintscan.io/celestia-incentivized-testnet/txs/$txhash"
    echo "----------------------------------------------------------------------"
} | tee -a output.log
