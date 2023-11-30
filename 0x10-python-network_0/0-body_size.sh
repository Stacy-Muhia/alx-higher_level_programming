#!/bin/bash
# size of body
curl -s "$1" | wc -c
