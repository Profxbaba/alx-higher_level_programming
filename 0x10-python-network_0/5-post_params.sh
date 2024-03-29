#!/bin/bash
# This script sends a POST request to the URL passed as the first argument with variables email and subject set to test@gmail.com and "I will always be here for PLD" respectively, and displays the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
