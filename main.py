import time
import json
from config.settings import API_TOKEN  
from strategies.moving_average import check_signal
from utils.data_fetcher import on_open, subscribe_to_ticks, on_error, on_close
from utils.trade_executor import execute_trade
from utils.logger import setup_logger
import websocket

prices = []
logger = setup_logger()

def on_message(ws, message):
    message = json.loads(message)
    if "tick" in message:
        tick = message["tick"]
        prices.append(tick['quote'])
        logger.info(f"Time: {tick['epoch']}, Price: {tick['quote']}")
        if len(prices) > 20:
            signal = check_signal(prices)
            if signal != "hold":
                execute_trade(ws, signal)
                prices.clear()

def run_bot():
    ws = websocket.WebSocketApp("wss://ws.binaryws.com/websockets/v3?app_id=1089",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = lambda ws: subscribe_to_ticks(ws, "CRASH_500")
    while True:
        try:
            ws.run_forever()
        except Exception as e:
            logger.error(f"Exception occurred: {e}")
            time.sleep(2)

if __name__ == "__main__":
    run_bot()
