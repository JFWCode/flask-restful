FROM python:3.8-alpine

LABEL maintainer="iAuto"

# install gcc env
RUN apk upgrade --update
RUN apk add --no-cache --virtual .build-deps gcc g++  python3-dev musl-dev libc-dev postgresql-dev
RUN pip install cython

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

ADD requirements.txt /

RUN pip install -r /requirements.txt

ADD src /src

EXPOSE 5000

WORKDIR /

#ENTRYPOINT ["/bin/bash"]
CMD ["python3", "-m", "src.run", "--host=0.0.0.0"]
