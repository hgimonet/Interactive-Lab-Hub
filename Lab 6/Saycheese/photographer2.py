import paho.mqtt.client as mqtt
import uuid
import queue
import time

# the # wildcard means we subscribe to all subtopics of IDD
sub_topic = 'IDD/Saycheese/#'

# some other examples
# topic = 'IDD/a/fun/topic'

# this is the callback that gets called once we connect to the broker.
# we should add our subscribe functions here as well
outputs = {}


def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(sub_topic)
    # todo: publish IDD/Saycheese/Photogrpher? ready, report status


# you can subsribe to as many topics as you'd like
# client.subscribe('some/other/topic')

message_queue = queue.Queue()

# this is the callback that gets called each time a message is recived
def on_message(client, userdata, msg):
    message_queue.put(msg.payload.decode('UTF-8'))
    # print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    # print(str(msg.topic))
    cam_idx = str(msg.topic)[-1]
    # print(cam_idx)
    outputs[cam_idx] = msg.payload.decode('UTF-8')
    # print(outputs)
    # todo: for every 'cam online, add camera

    # you can filter by topics


# if msg.topic == 'IDD/some/other/topic': do thing

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

# connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

## ------------- TO SEND MESSAGES

val = "don't take picture"


photo = set(outputs.values())
print(photo)
if len(photo) == 1:
    if list(photo)[0] == "ready":
        val = "take picture"

print(val)

pub_topic = "IDD/Saycheese/TakePic"

# while True:
#     client.publish(topic, message)

if val == "take picture":
    client.publish(pub_topic, val)

# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_start()
print("beyond the loop!")

curr_state = 'check cameras'
timer = time.time()

while True:
    # message handling part
    while not message_queue.empty():
        print(message_queue.get(), 'test')
        if curr_state == 'check cameras':
            # todo: save any new camera to dict
        if curr_state == 'wait for smiles':
            # todo: check all cams smiling and send photo message
    # state change handling
    # update curr state
    if curr_state == 'check cameras':
        time_passed = time.time()-timer
        if time_passed >= 5:
            # todo: send message that cameras to report when ready
            # reset timer
            timer = time.time()
            curr_state = 'wait for smiles'
        pass
    elif True:
        pass

    time.sleep(0.1)
    pass
