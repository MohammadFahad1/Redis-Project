import redis

r = redis.Redis()
pubsub = r.pubsub()

pubsub.subscribe('notifications')

for message in pubsub.listen():
    print("Notification: ", message['data'])