# Pull a lean base image
FROM python:3.8-alpine
# We need the "ip" command used in 'start.sh'
RUN apk add --update iproute2
COPY start.sh /
RUN chmod +x /start.sh
COPY ./quoteserver /quoteserver
# requirements.txt lists the modules & their versions to be installed
RUN pip install --upgrade pip
RUN pip install -r ./quoteserver/requirements.txt
# Update /etc/hosts and start gunicorn
CMD ["/start.sh"]

