#!/usr/bin/env python3

'''CSP Class for the Privacy Preserving Ridge Regression'''

__author__ = "William CLOT, www.github.com/williamclot; Camille PLAYS, www.github.com/camilleplays"
__license__ = "MIT"
__date__ = "13/11/2018"

# import pandas as pd
from phe import paillier
import numpy as np
import math
import sys
import socket, pickle

# System import classes folder as well
sys.path.insert(0,'./classes/')

from utils import termcol as tc
from utils import utils
from utils import members
from utils import parameters 

u = utils();

##---------* Functions *----------##

class CSP:
    def __init__(self, verbose=False, encrypt=False):
        # Programm parameters
        self.verbose = verbose
        self.encrypt = encrypt

        if (self.verbose): print(tc.WARNING+"Initiating the CSP [-]"+tc.ENDC)

        # Generate the public and private key used for Paillier encryption and decryption
        self.public_key, self.private_key = paillier.generate_paillier_keypair()
        if (self.verbose): print(tc.OKGREEN+"\t --> Key pair generated"+tc.ENDC)

        # Sending public_key to the Users and CSP
        u.sendViaSocket(members.Users, self.public_key, '\t --> Sending public key to Users')
        u.sendViaSocket(members.Evaluator, self.public_key, '\t --> Sending public key to Evaluator')

        [self.Amask, self.bmask] = u.receiveViaSocket(members.CSP, '\t --> Receiving Amask and bmask')
        if(self.encrypt):
            self.Amask = self.decrypt(Amask)
            self.bmask = self.decrypt(bmask)
        
        u.ParseToFile(self.Amask, "garbled_circuit/inputs/Amask")
        u.ParseToFile(self.bmask, "garbled_circuit/inputs/bmask")

CSP = CSP(verbose=parameters.verbose, encrypt=parameters.encrypt)