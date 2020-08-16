FROM stormpy
RUN mkdir /opt/gridworld
WORKDIR /opt/gridworld

RUN apt-get install -y ffmpeg

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN python setup.py install

