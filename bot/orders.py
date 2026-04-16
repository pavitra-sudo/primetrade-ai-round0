from bot.client import BinanceClient
from bot.validators import OrderInput

client = BinanceClient()

def place_order(symbol, side, order_type, quantity, price=None):
    # Validate input
    order = OrderInput(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    payload = {
        "symbol": order.symbol,
        "side": order.side,
        "type": order.order_type,
        "quantity": order.quantity,
    }

    if order.order_type == "LIMIT":
        payload["price"] = order.price
        payload["timeInForce"] = "GTC"

    response = client.place_order(payload)

    return {
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice", "N/A")
    }