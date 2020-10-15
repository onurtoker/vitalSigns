import uhd
from uhd import libpyuhd as lib
import numpy as np
import scipy.io
import threading
import matplotlib.pyplot as plt
import time
from timeit import default_timer as timer

from myConstants import *
from myGUI import *
import myUSRP

# USRP selection
usrpTX = myUSRP.Device("serial=30B0CED")
#usrpTX.usrp.set_clock_source('external')
usrpRX = myUSRP.Device("serial=30B0CED")
#usrpRX.usrp.set_clock_source('external')

usrpTX.set_tx_config(fLO, fs, channelsTX, gainTX)
usrpRX.set_rx_config(fLO, fs, channelsRX, gainRX)
tx_buffer = 0.7 * np.array(np.exp(2j*np.pi*np.arange(0,ns)/ndiv), dtype=np.complex64)
usrpTX.start_tx_stream(tx_buffer)
usrpRX.start_rx_stream()

pvals = np.zeros(ns)
dphase = 0
loop_index = 0

while True:
    loop_index = loop_index + 1

    # Read
    (x0,) = usrpRX.get_rx_buffer()

    # DSP
    X0 = np.fft.fftshift(np.fft.fft(x0, hrf * ns))
    S0 = 10 * np.log(np.abs(X0) / np.sqrt(ns))
    k = np.argmax(S0)

    dphase = 180 / np.pi * np.angle(X0[k])

    mplt0i.set_ydata(np.real(x0))
    mplt0q.set_ydata(np.imag(x0))

    pvals = np.concatenate((dphase, pvals[0:ns-1]), axis=None)
    mplt0s.set_ydata(pvals)
    refresh()


usrpTX.stop_tx_stream()
usrpRX.stop_rx_stream()


