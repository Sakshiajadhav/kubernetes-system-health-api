#!/bin/bash

URL=${1:-http://localhost:30007/health}

echo "Checking health endpoint: $URL"

response=$(curl -s "$URL")

if [ -z "$response" ]; then
  echo "No response from application"
  exit 1
fi

echo "$response"