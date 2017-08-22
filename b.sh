#!/usr/bin/env bash

rm -rf build/*
sphinx-build -W -b dirhtml . build
