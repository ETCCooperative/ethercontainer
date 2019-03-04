FROM ubuntu:xenial
LABEL MAINTAINER="Yaz Khoury <yaz@etccooperative.org>"

# install tools and dependencies
RUN apt update && apt install -y --no-install-recommends openssl libudev-dev file curl jq wget net-tools

ENV RUST_BACKTRACE 1

RUN apt autoremove -y \
  && apt clean -y \
  && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

RUN groupadd -g 1000 parity \
  && useradd -m -u 1000 -g parity -s /bin/sh parity

WORKDIR /home/parity

COPY artifacts/x86_64-unknown-linux-gnu/parity /bin/parity

COPY scripts/docker/hub/check_sync.sh /check_sync.sh

USER parity

EXPOSE 5001 8080 8082 8083 8545 8546 8180 30303/tcp 30303/udp

ENTRYPOINT ["/bin/parity"]
