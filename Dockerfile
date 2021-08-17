FROM python:3.6-slim
RUN apt-get update \
    && apt-get install --no-install-recommends -y dirmngr gnupg apt-transport-https ca-certificates \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
    && sh -c 'echo "deb https://download.mono-project.com/repo/debian stable-buster main" > /etc/apt/sources.list.d/mono-official-stable.list' \
    && apt-get update -y \
    && apt-get install --no-install-recommends -y mono-devel clang libglib2.0-dev nuget gcc g++\
    && pip install -U --no-cache-dir pip pycparser setuptools \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /code
COPY . .
COPY PricingData PricingData
RUN apt-get update -y \
    && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]