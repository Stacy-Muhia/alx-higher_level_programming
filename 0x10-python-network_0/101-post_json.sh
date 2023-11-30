#!/bin/bash
# sends a JSON POST request to a URL passed and displays response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
