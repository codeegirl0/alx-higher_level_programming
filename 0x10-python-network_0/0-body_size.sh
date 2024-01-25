#!/bin/bash
# sending reqs
curl -s "$1" | wc -c
