from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession
from autobahn.wamp.exception import ApplicationError

import subprocess


class AppSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):


        def drinkmotherfucker(msg):
            print("DrINK MUTHERFUCKER CALLED! {}".format(msg))
            print(self.imageMagic())
            return "DRUNK"

        reg = yield self.register(drinkmotherfucker, 'com.barfly.drinkmotherfucker')
        print("procedure DRINKMOTHERFUCKER() registered: {}".format(reg))


    def imageMagic(self):
        # return "called da magic.."
        # return subprocess.check_output(["echo", "Calling Da Magic!"])
        return subprocess.check_output(["/usr/bin/streamer", "-o", "filezz.jpg", "-s", "480-180"])
