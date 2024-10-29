FROM python:3.11-bookworm as lambda

WORKDIR /workspace

RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev \
  libgl1-mesa-glx \
  libglib2.0-0

RUN pip install flask carvekit awslambdaric --extra-index-url https://download.pytorch.org/whl/cpu

COPY patches.py /usr/local/lib/python3.11/site-packages/carvekit/ml/files/__init__.py

COPY . .

RUN python predict.py

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]

CMD [ "lambda.handler" ]
