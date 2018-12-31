#!/bin/sh
lipc-set-prop com.lab126.pillow disableEnablePillow enable&
ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill -9
