#!/bin/bash
socat TCP-LISTEN:6969,reuseaddr,fork EXEC:"./example"
