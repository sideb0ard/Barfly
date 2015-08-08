from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession
from autobahn.wamp.exception import ApplicationError

import os
import subprocess
import time


class AppSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):


        def drinkmotherfucker(msg):
            print("DrINK MUTHERFUCKER CALLED! {}".format(msg))
            return(self.imageMagic())

        reg = yield self.register(drinkmotherfucker, 'com.barfly.drinkmotherfucker')
        print("procedure DRINKMOTHERFUCKER() registered: {}".format(reg))


    def imageMagic(self):
        # return "called da magic.."
        # return subprocess.check_output(["echo", "Calling Da Magic!"])
        # return os.getcwd()
        ofilename = "filezzz" + str(int(time.time())) + ".jpeg"
        ofile = "/usr/local/Barfly/webby/hello/web/fileoutput/" + ofilename
        subprocess.check_output(["/usr/bin/streamer", "-o", ofile, "-s", "480x180"])
        return ofilename
