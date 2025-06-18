import json
import uvicorn


if __name__ == "__main__":
    with open("uvicorn_config.json") as f:
        config = json.load(f)

    uvicorn.run(app=config['app'],
                host=config['host'], port=config['port'],
                reload=config['reload'],
                log_level=config['log_level'],
                workers=config['workers'])
