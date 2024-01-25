#!/bin/bash
# sending request 
curl -s -o /dev/null -w "%{http_code}" "$1"
