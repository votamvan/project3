# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# install and cache app dependencies
COPY package.json package.json

RUN npm install
RUN npm install @vue/cli@3.7.0 -g

#if we want to run development mode
COPY ./ ./
# start app
CMD ["npm", "run", "dev"]


#if we want to run in production mode then we copy only dist folder
# COPY ./ ./
# RUN npm install -g serve
# start app
# CMD [ "serve","-p","8081","-s", "dist" ]


# docker build -t front .
# docker run -it -p 8081:8081 front