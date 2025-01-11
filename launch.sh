#!/bin/bash

source ./venv/bin/activate

dvc add data/processed/data.csv

dvc repro

dvc metrics show

dvc push
