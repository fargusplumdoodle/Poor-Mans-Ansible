#!/bin/bash
GLOBAL='ay this works'

function success {
	echo success $GLOBAL
	return 0 
}

function fail {
	echo success $GLOBAL
	return 1 
}

function main {
	success
	fail
}
