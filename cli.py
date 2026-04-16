import typer
from bot.orders import place_order

app = typer.Typer()

@app.command()
def trade(
    symbol: str = typer.Option(..., "--symbol"),
    side: str = typer.Option(..., "--side"),
    order_type: str = typer.Option(..., "--order-type"),
    quantity: float = typer.Option(..., "--quantity"),
    price: float = typer.Option(None, "--price")
):
    try:
        result = place_order(symbol, side, order_type, quantity, price)

        print("\n=== ORDER SUMMARY ===")
        print(result)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    app()