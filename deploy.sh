#!/usr/bin/env bash

cd api/
sh build-api.sh
cd ../

cd db/
sh build-db.sh
cd ../

cd html/
sh build-ui.sh
cd ../

kubectl apply -f kube-deployment.yml