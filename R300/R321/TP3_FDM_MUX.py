#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Multiplexeur fréquence Rx21
# Author: Philippe PUJAS
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class TP3_FDM_MUX(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multiplexeur fréquence Rx21", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multiplexeur fréquence Rx21")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "TP3_FDM_MUX")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1920000/2
        self.num_canal_C = num_canal_C = 3
        self.num_canal_B = num_canal_B = 2
        self.num_canal_A = num_canal_A = 0
        self.chsp = chsp = 15000
        self.ch0 = ch0 = 50000
        self.canal_a_1 = canal_a_1 = 0
        self.BP = BP = 18000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0_1_0 = qtgui.freq_sink_f(
            4096, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            3,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_0.set_y_axis(-150, 10)
        self.qtgui_freq_sink_x_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1_0.set_plot_pos_half(not True)

        labels = ['v1', 'v2', 'Mux', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_0_win)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_f(
            4096, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            3,
            None # parent
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-150, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['v1', 'v2', 'Mux', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            4096, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-150, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['c1', 'trc1', 'v1', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_wavfile_source_0_0_0 = blocks.wavfile_source('/home/bastien/But-1ere-annee/R300/R321/12-960k.wav', True)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('/home/bastien/But-1ere-annee/R300/R321/09-960k.wav', True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/bastien/But-1ere-annee/R300/R321/04-960k.wav', True)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, ch0+num_canal_C*chsp, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, ch0+num_canal_B*chsp, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, ch0+num_canal_A*chsp, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0_1_0, 2))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.qtgui_freq_sink_x_0_1_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.qtgui_freq_sink_x_0_1_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.qtgui_freq_sink_x_0_1, 1))
        self.connect((self.blocks_wavfile_source_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_wavfile_source_0_0_0, 0), (self.qtgui_freq_sink_x_0_1, 2))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TP3_FDM_MUX")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)

    def get_num_canal_C(self):
        return self.num_canal_C

    def set_num_canal_C(self, num_canal_C):
        self.num_canal_C = num_canal_C
        self.analog_sig_source_x_0_0_0.set_frequency(self.ch0+self.num_canal_C*self.chsp)

    def get_num_canal_B(self):
        return self.num_canal_B

    def set_num_canal_B(self, num_canal_B):
        self.num_canal_B = num_canal_B
        self.analog_sig_source_x_0_0.set_frequency(self.ch0+self.num_canal_B*self.chsp)

    def get_num_canal_A(self):
        return self.num_canal_A

    def set_num_canal_A(self, num_canal_A):
        self.num_canal_A = num_canal_A
        self.analog_sig_source_x_0.set_frequency(self.ch0+self.num_canal_A*self.chsp)

    def get_chsp(self):
        return self.chsp

    def set_chsp(self, chsp):
        self.chsp = chsp
        self.analog_sig_source_x_0.set_frequency(self.ch0+self.num_canal_A*self.chsp)
        self.analog_sig_source_x_0_0.set_frequency(self.ch0+self.num_canal_B*self.chsp)
        self.analog_sig_source_x_0_0_0.set_frequency(self.ch0+self.num_canal_C*self.chsp)

    def get_ch0(self):
        return self.ch0

    def set_ch0(self, ch0):
        self.ch0 = ch0
        self.analog_sig_source_x_0.set_frequency(self.ch0+self.num_canal_A*self.chsp)
        self.analog_sig_source_x_0_0.set_frequency(self.ch0+self.num_canal_B*self.chsp)
        self.analog_sig_source_x_0_0_0.set_frequency(self.ch0+self.num_canal_C*self.chsp)

    def get_canal_a_1(self):
        return self.canal_a_1

    def set_canal_a_1(self, canal_a_1):
        self.canal_a_1 = canal_a_1

    def get_BP(self):
        return self.BP

    def set_BP(self, BP):
        self.BP = BP




def main(top_block_cls=TP3_FDM_MUX, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
