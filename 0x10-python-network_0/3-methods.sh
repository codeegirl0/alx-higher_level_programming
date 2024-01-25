#!/bin/bash
# show HTTP method
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
