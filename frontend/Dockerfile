FROM node:22-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN chmod +x docker-entrypoint.sh

EXPOSE 5173

ENTRYPOINT ["./docker-entrypoint.sh"]
