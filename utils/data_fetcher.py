import json
import logging
from config.settings import API_TOKEN

logger = logging.getLogger(__name__)

def on_open(ws):
    logger.info("Connection opened")
    auth_data = {
        "authorize": API_TOKEN
    }
    ws.send(json.dumps(auth_data))

def subscribe_to_ticks(ws, symbol="R_50"):
    tick_request = {
        "ticks": symbol,
        "subscribe": 1
    }
    ws.send(json.dumps(tick_request))

def on_error(ws, error):
    logger.error(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    logger.info(f"Connection closed: {close_status_code} - {close_msg}")
