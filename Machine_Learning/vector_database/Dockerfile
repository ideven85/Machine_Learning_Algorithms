FROM postgres:latest

RUN apt-get update && \
    apt-get install -y build-essential postgresql-server-dev-all git && \
    git clone --branch v0.7.3 https://github.com/pgvector/pgvector.git && \
    cd pgvector && \
    make && \
    make install && \
    cd .. && \
    rm -rf pgvector && \
    apt-get remove -y build-essential postgresql-server-dev-all && \
    apt-get autoremove -y && \
    apt-get clean