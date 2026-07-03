FROM node:22-alpine
WORKDIR /app

ARG VITE_API_BASE=http://backend:8080
ENV VITE_API_BASE=$VITE_API_BASE

RUN corepack enable && corepack prepare pnpm@latest --activate

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

COPY . .
RUN pnpm build

EXPOSE 3000
ENV HOST=0.0.0.0
ENV PORT=3000
CMD ["node", "build"]
