FROM node
WORKDIR /app
RUN npm install -g @vue/cli
COPY . .
EXPOSE 8080
