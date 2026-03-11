#!/bin/bash

echo "Running Bandit security scan..."
python -m bandit -r app

echo "Checking dependencies with Safety..."
python -m safety check