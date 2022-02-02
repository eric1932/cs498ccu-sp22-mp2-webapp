#!/bin/bash
set -eo pipefail
VENV_DIR_NAME="venv"

if [[ ! -d ${VENV_DIR_NAME} ]]
then
  echo "Initialize Python venv"
  python3 -m venv ${VENV_DIR_NAME}
fi

echo "Activate venv"
source ${VENV_DIR_NAME}/bin/activate
pip3 install -r requirements.txt

uvicorn main:app --host 0.0.0.0 --port 80
