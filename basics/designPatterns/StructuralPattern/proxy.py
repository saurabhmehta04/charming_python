import time


class Producer:
    ''' Define the 'resource-intensive' object to instantiate'''

    def producer(self):
        print("Producer is working hard")

    def meet(self):
        print("producer has time to meet you now")


class Proxy:
    ''' Define the 'relatively less resource-intensive' proxy to instantiate as a middleman'''

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        ''' Check if the producer is available'''
        print("Artist checking if producer is available")

        if self.occupied == "No":
            # if the producer is available, create a producer object !
            self.producer = Producer()
            time.sleep(2)
            # make the producer meet the guest !
            self.producer.meet()

        else:
            # otherwise, dont instantiate the producer
            time.sleep(2)
            print("Producer is busy")


# Instantiate the proxy
p = Proxy()

# Make the proxy: Artist produce until Producer is available
p.produce()

# change the state to "occupied"
p.occupied = 'YES'

# make the producer produce
p.produce()
