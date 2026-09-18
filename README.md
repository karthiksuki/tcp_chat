# tcp-chat

A tiny TCP chat room. One server, many clients. No extra libraries.

## Flow

```
you type a name  →  client connects  →  server asks NAME
                 ←  you send your name
                 ←  everyone sees "joined"
you type a line  →  server broadcasts it to all clients
you disconnect   →  everyone sees "left"
```

1. Start the server. It listens on `localhost:5500`.
2. Start a client. It asks for a nickname, then connects.
3. The server greets that client and tells everyone else they joined.
4. Anything you type is sent as `nickname : message` and relayed to every connected client.
5. If a client drops, the server removes them and tells the room.

Two terminals is enough: one for the server, one (or more) for clients.

## Run

Python 3.14+. From the project root:

```bash
python server.py
```

In another terminal:

```bash
python client.py
```

Type a nickname, then chat. Open more `python client.py` terminals to add people.

Stop with `Ctrl+C`.
