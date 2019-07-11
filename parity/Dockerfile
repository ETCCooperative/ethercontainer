FROM ubuntu:xenial
LABEL MAINTAINER="Yaz Khoury <yaz@etccooperative.org>"

# install tools and dependencies
RUN apt update && apt install -y --no-install-recommends openssl libudev-dev file curl jq wget net-tools

ENV RUST_BACKTRACE 1

# install tools and dependencies
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		file curl jq; \
# apt cleanup
	apt-get autoremove -y; \
	apt-get clean; \
	rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*; \
# add user
	groupadd -g 1000 parity; \
	useradd -m -u 1000 -g parity -s /bin/sh parity

WORKDIR /home/parity

ENV PARITY_URL="https://releases.parity.io/ethereum/v2.6.0/x86_64-unknown-linux-gnu/parity"
RUN wget --no-check-certificate $PARITY_URL && mv parity /bin/parity
#COPY parity /bin/parity
RUN chmod +x /bin/parity

COPY check_sync.sh /check_sync.sh

COPY morden_reserved.txt /morden_reserved.txt

USER parity

EXPOSE 5001 8080 8082 8083 8545 8546 8180 30303/tcp 30303/udp

ENTRYPOINT ["/bin/parity"]
