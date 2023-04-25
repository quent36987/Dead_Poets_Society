import redis

r = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

print("Hello, World!", flush=True)
print(r.ping())
print("Hello, World!", flush=True)

# pubsub() method creates the pubsub object
# but why i named it mobile 🧐
# just kidding 😂 think of it as the waki taki that listens for incomming messages
mobile = r.pubsub()

# use .subscribe() method to subscribe to topic on which you want to listen for messages
mobile.subscribe('my-channel')

# .listen() returns a generator over which you can iterate and listen for messages from publisher

for message in mobile.listen():
    print(message) # <-- you can literally do any thing with this message i am just printing it
