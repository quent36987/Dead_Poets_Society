import redis

r = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

mobile = r.pubsub()
mobile.subscribe('new_user')

for message in mobile.listen():
    print(f'New user: {message["data"]}')
