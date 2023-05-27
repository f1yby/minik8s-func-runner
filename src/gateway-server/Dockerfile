FROM ubuntu:latest
RUN apt update && apt install -y nginx
COPY bnc.awk run.sh ./
# CMD ["nginx", "-g", "daemon off;"]
CMD bash run.sh
