FROM nginx:alpine
# ADD ./index.html /var/www/html/ (dont copy to this path this for os systems like ubuntu where apache is running for the nginx container the the path is usr/share/nginx/html/index.html. you dont need to rm the default app as nginx will automatically overwrites it!)
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80