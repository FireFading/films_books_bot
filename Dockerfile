FROM python:3.11-bullseye

WORKDIR /bot

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99
ENV TZ=Europe/Moscow

ENV PYTHONPATH=/bot/

COPY ./requirements.txt /bot/

# RUN apt-get update && apt-get install -yq \
#     curl \
#     unzip \
#     xvfb \
#     libxi6 \
#     libgconf-2-4 \
#     default-jdk \
#     wget

# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -yq ./google-chrome-stable_current_amd64.deb


# RUN curl https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chromedriver-linux64.zip --output /tmp/chromedriver_linux64.zip \
#     && unzip /tmp/chromedriver_linux64.zip -d /usr/bin/ \
#     && rm /tmp/chromedriver_linux64.zip

# RUN ln -s /usr/bin/chromedriver-linux64/chromedriver && chmod 777 /usr/bin/chromedriver-linux64/chromedriver

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

