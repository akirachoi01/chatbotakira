import websocket

def on_message(ws, message):
    print(f"Bot says: {message}")

def on_open(ws):
    print("Connection opened. Sending test messages...")
    ws.send("Tell me a story about a brave knight.")
    ws.send("Translate 'Hello' into French.")
    ws.send("Summarize the history of space exploration.")

ws = websocket.WebSocketApp("ws://192.168.10.207:5000", on_message=on_message)

ws.run_forever()
