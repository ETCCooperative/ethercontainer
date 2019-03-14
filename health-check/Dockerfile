FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*


ENV URL="https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/v0.2.0/grpc_health_probe-linux-amd64"

RUN wget $URL --no-check-certificate && \ 
    mv grpc_health_probe-linux-amd64 /bin/ && \
    chmod +x /bin/grpc_health_probe-linux-amd64
