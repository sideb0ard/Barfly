from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession
from autobahn.wamp.exception import ApplicationError


class AppSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):

        # SUBSCRIBE to a topic and receive events
        #
        def onhello(msg):
            print("event for 'onhello' received: {}".format(msg))

        sub = yield self.subscribe(onhello, 'com.barfly.onhello')
        print("subscribed to topic 'onhello': {}".format(sub))


        def drinkmotherfucker(msg):
            print("DrINK MUTHERFUCKER CALLED! {}".format(msg))
            return "DRUNK"

        reg = yield self.register(drinkmotherfucker, 'com.barfly.drinkmotherfucker')
        print("procedure DRINKMOTHERFUCKER() registered: {}".format(reg))



        # PUBLISH and CALL every second .. forever
        #
        counter = 0
        while True:

            # PUBLISH an event
            #
            yield self.publish('com.barfly.oncounter', counter)
            print("published to 'oncounter' with counter {}".format(counter))
            counter += 1

            # CALL a remote procedure
            #
            try:
                res = yield self.call('com.barfly.mul2', counter, 3)
                print("mul2() called with result: {}".format(res))
            except ApplicationError as e:
                # ignore errors due to the frontend not yet having
                # registered the procedure we would like to call
                if e.error != 'wamp.error.no_such_procedure':
                    raise e

            yield sleep(1)
