# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# install and cache app dependencies
COPY package.json package.json

RUN npm install
RUN npm install @vue/cli@3.7.0 -g

#if we want to run development mode
COPY public/ public/
COPY src/ src/
# start app
CMD ["npm", "run", "serve"]

#if we want to run in production mode then we copy only dist folder

#RUN npm install -g serve
#COPY public/ public/
#COPY src/ src/
#RUN npm run build
#COPY dist/ dist/
# start app
#CMD [ "serve","-p","3838","-s", "dist" ]


# docker build -t front .
# docker run -it -v /app -v /app -p 8081:8080 front