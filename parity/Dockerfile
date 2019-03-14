FROM ubuntu:xenial
LABEL MAINTAINER="Yaz Khoury <yaz@etccooperative.org>"

# install tools and dependencies
RUN apt update && apt install -y --no-install-recommends openssl libudev-dev file curl jq wget net-tools python-pip

ENV RUST_BACKTRACE 1

RUN apt autoremove -y \
  && apt clean -y \
  && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

RUN groupadd -g 1000 parity \
  && useradd -m -u 1000 -g parity -s /bin/sh parity

WORKDIR /home/parity

ENV PARITY_URL="https://releases.parity.io/ethereum/v2.3.5/x86_64-unknown-linux-gnu/parity"
RUN wget --no-check-certificate $PARITY_URL && chmod u+x parity && mv parity /bin/parity

RUN pip install requests
COPY check_sync.sh /check_sync.sh
COPY etherhealth.py /etherhealth.py

USER parity

EXPOSE 5001 8080 8082 8083 8545 8546 8180 30303/tcp 30303/udp

ENTRYPOINT ["/bin/parity"]
