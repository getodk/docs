#!/usr/bin/env bash

rm -rf build/*
sphinx-build -b dirhtml . build
sphinx-build -b pdf . build       


