FROM python:3
WORKDIR /usr/src/app
ENV path "/mnt/shared_from_host"
RUN /bin/echo "Hello $name"
RUN ["/bin/bash", "-c", "echo Hello $name"]
COPY . .
CMD ["test_sum_num.py"]
ENTRYPOINT [ "python3"]