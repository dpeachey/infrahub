# Infrahub

```
docker compose -f infrahub/docker-compose.yml -f docker-compose.override.yml -p infrahub up -d
uv run infrahubctl repository add local /upstream
```