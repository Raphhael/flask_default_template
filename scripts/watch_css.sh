#!/bin/bash

. ./config
cd $base_dir/app/static/style
sass --watch style.scss:style.css

