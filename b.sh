#!/usr/bin/env bash

rm -rf build/*
sphinx-build -b dirhtml . build

