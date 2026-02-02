# Endpoints

## Health

### GET /health
```json
{"status": "healthy", "version": "0.1.0"}
```

## Dice

### POST /dice/roll
```json
{
  "notation": "2d6+3",
  "count": 1
}
```

Response:
```json
{
  "results": [11],
  "proof": "a1b2c3..."
}
```

## Economy

### GET /economy/balance
```json
{"credits": 1000, "used_today": 50}
```

## Oracle

### POST /oracle/predict
```json
{
  "my_list": {...},
  "opponent_list": {...}
}
```

Response:
```json
{
  "probability": 0.62,
  "confidence": 0.08
}
```
