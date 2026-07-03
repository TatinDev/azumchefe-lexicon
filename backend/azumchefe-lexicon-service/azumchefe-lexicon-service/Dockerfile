FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:10.0 AS build
ARG TARGETARCH
WORKDIR /src

COPY src/Azumchefe.API/*.csproj src/Azumchefe.API/
COPY src/Azumchefe.Application/*.csproj src/Azumchefe.Application/
COPY src/Azumchefe.Domain/*.csproj src/Azumchefe.Domain/
COPY src/Azumchefe.Infrastructure/*.csproj src/Azumchefe.Infrastructure/
RUN dotnet restore -a $TARGETARCH src/Azumchefe.API/*.csproj

COPY src/ ./src/
RUN dotnet publish -a $TARGETARCH src/Azumchefe.API/*.csproj --no-restore -o /app

FROM mcr.microsoft.com/dotnet/aspnet:10.0
WORKDIR /app

COPY srv/ /srv/
COPY --from=build /app .

EXPOSE 8080
ENV ASPNETCORE_URLS=http://+:8080
ENV Azumchefe__LexiconPath=/srv/azumchefe/public/
ENTRYPOINT ["./azumchefed"]
