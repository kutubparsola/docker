FROM node
WORKDIR app/
ADD package.json .
RUN npm install
COPY  . .
EXPOSE 3000
CMD [ "npm","start" ]

# mistakes :-
#     1. used ubuntu image instead of node image just because i thaught like mvn install where u need to use java image and with that you pass mvn install cmd. so yeahhh huh
#     2. mistaken package.json as just instruction instead it was list of dependensis which is why u run npm install 
#     3. define work dir as home/ubuntu but you can give any so.
#     now main thing is that why using CMD instead of ENTRYPOINT? so as we know that we can also enter the container through docker exex cmd so if the user want to replace the npm start(whole npm start not only start) with /bin/bash they can do so but with entrypoint this become strict.
