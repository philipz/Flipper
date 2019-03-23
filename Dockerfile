  FROM centos:7.5
  LABEL MAINTAINER  ajeetraina@gmail.com
  
  RUN yum update -y
  RUN yum install -y httpd
  COPY cgi-bin /var/www/cgi-bin/
  COPY html  /var/www/html/
  
  CMD ["./wrapper.sh"]