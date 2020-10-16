#!/bin/bash

. ./config
cd $base_dir
flask run --host=$server_host
