import json
import logging

logger = logging.getLogger(__name__)

def execute_trade(ws, signal):
    trade_request = {
        "buy": 1 if signal == "buy" else 0,
        "sell": 1 if signal == "sell" else 0,
        "amount": 10,  # example amount
        "symbol": "R_100",
        "duration": 5,
        "basis": "stake",
        "contract_type": "CALL" if signal == "buy" else "PUT",
        "currency": "USD"
    }
    ws.send(json.dumps(trade_request))
    logger.info(f"Trade executed: {trade_request}")
