#!/usr/bin/env bash

rm -rf build/*
python style-test.py
sphinx-build -b spelling src build/spelling
sphinx-build -b dirhtml src build
