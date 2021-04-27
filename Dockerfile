FROM sjunges/stormpy:1.6.4
RUN mkdir /opt/gridstorm
WORKDIR /opt/gridstorm

RUN apt-get install -y ffmpeg

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN python setup.py install

