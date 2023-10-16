#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Oct 16 11:52:53 2023
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.b5 = b5 = 1
        self.b4 = b4 = 1
        self.b3 = b3 = 1
        self.b2 = b2 = 1
        self.b1 = b1 = 1
        self.a5 = a5 = 0
        self.a4 = a4 = 0
        self.a3 = a3 = 0
        self.a2 = a2 = 0
        self.a1 = a1 = 0
        self.a0 = a0 = 1
        self.Freq_fondamentale = Freq_fondamentale = 1000

        ##################################################
        # Blocks
        ##################################################
        self._b5_range = Range(-2, 2, 0.1, 1, 200)
        self._b5_win = RangeWidget(self._b5_range, self.set_b5, 'b5', "slider", float)
        self.top_layout.addWidget(self._b5_win)
        self._b4_range = Range(-2, 2, 0.1, 1, 200)
        self._b4_win = RangeWidget(self._b4_range, self.set_b4, 'b4', "slider", float)
        self.top_layout.addWidget(self._b4_win)
        self._b3_range = Range(-2, 2, 0.1, 1, 200)
        self._b3_win = RangeWidget(self._b3_range, self.set_b3, 'b3', "slider", float)
        self.top_layout.addWidget(self._b3_win)
        self._b2_range = Range(-2, 2, 0.1, 1, 200)
        self._b2_win = RangeWidget(self._b2_range, self.set_b2, 'b2', "slider", float)
        self.top_layout.addWidget(self._b2_win)
        self._b1_range = Range(-2, 2, 0.1, 1, 200)
        self._b1_win = RangeWidget(self._b1_range, self.set_b1, 'b1', "slider", float)
        self.top_layout.addWidget(self._b1_win)
        self._a5_range = Range(-2, 2, 0.1, 0, 200)
        self._a5_win = RangeWidget(self._a5_range, self.set_a5, 'a5', "slider", float)
        self.top_layout.addWidget(self._a5_win)
        self._a4_range = Range(-2, 2, 0.1, 0, 200)
        self._a4_win = RangeWidget(self._a4_range, self.set_a4, 'a4', "slider", float)
        self.top_layout.addWidget(self._a4_win)
        self._a3_range = Range(-2, 2, 0.1, 0, 200)
        self._a3_win = RangeWidget(self._a3_range, self.set_a3, 'a3', "slider", float)
        self.top_layout.addWidget(self._a3_win)
        self._a2_range = Range(-2, 2, 0.1, 0, 200)
        self._a2_win = RangeWidget(self._a2_range, self.set_a2, 'a2', "slider", float)
        self.top_layout.addWidget(self._a2_win)
        self._a1_range = Range(-2, 2, 0.1, 0, 200)
        self._a1_win = RangeWidget(self._a1_range, self.set_a1, 'a1', "slider", float)
        self.top_layout.addWidget(self._a1_win)
        self._a0_range = Range(-2, 2, 0.1, 1, 200)
        self._a0_win = RangeWidget(self._a0_range, self.set_a0, 'a0', "slider", float)
        self.top_layout.addWidget(self._a0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_throttle_0_1_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, 0, a0, 0)
        self.analog_sig_source_x_0_1_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 5*Freq_fondamentale, a5, 0)
        self.analog_sig_source_x_0_1_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 4*Freq_fondamentale, a4, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 3*Freq_fondamentale, a3, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 2*Freq_fondamentale, a2, 0)
        self.analog_sig_source_x_0_0_0_0_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 5*Freq_fondamentale, b5, 0)
        self.analog_sig_source_x_0_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 4*Freq_fondamentale, b4, 0)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 3*Freq_fondamentale, b3, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 2*Freq_fondamentale, b2, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, Freq_fondamentale, b1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, Freq_fondamentale, a1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_0_0, 0), (self.blocks_throttle_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_0_1, 0), (self.blocks_throttle_0_0_0_0_1, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_throttle_0_1_0, 0))
        self.connect((self.analog_sig_source_x_0_1_0_0, 0), (self.blocks_throttle_0_1_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1_0_1, 0), (self.blocks_throttle_0_1_0_1, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.blocks_throttle_0_0_0_0_0, 0), (self.blocks_add_xx_0, 8))
        self.connect((self.blocks_throttle_0_0_0_0_1, 0), (self.blocks_add_xx_0, 10))
        self.connect((self.blocks_throttle_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_throttle_0_1_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_throttle_0_1_0_0, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.blocks_throttle_0_1_0_1, 0), (self.blocks_add_xx_0, 9))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0_1_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_b5(self):
        return self.b5

    def set_b5(self, b5):
        self.b5 = b5
        self.analog_sig_source_x_0_0_0_0_1.set_amplitude(self.b5)

    def get_b4(self):
        return self.b4

    def set_b4(self, b4):
        self.b4 = b4
        self.analog_sig_source_x_0_0_0_0_0.set_amplitude(self.b4)

    def get_b3(self):
        return self.b3

    def set_b3(self, b3):
        self.b3 = b3
        self.analog_sig_source_x_0_0_0_0.set_amplitude(self.b3)

    def get_b2(self):
        return self.b2

    def set_b2(self, b2):
        self.b2 = b2
        self.analog_sig_source_x_0_0_0.set_amplitude(self.b2)

    def get_b1(self):
        return self.b1

    def set_b1(self, b1):
        self.b1 = b1
        self.analog_sig_source_x_0_0.set_amplitude(self.b1)

    def get_a5(self):
        return self.a5

    def set_a5(self, a5):
        self.a5 = a5
        self.analog_sig_source_x_0_1_0_1.set_amplitude(self.a5)

    def get_a4(self):
        return self.a4

    def set_a4(self, a4):
        self.a4 = a4
        self.analog_sig_source_x_0_1_0_0.set_amplitude(self.a4)

    def get_a3(self):
        return self.a3

    def set_a3(self, a3):
        self.a3 = a3
        self.analog_sig_source_x_0_1_0.set_amplitude(self.a3)

    def get_a2(self):
        return self.a2

    def set_a2(self, a2):
        self.a2 = a2
        self.analog_sig_source_x_0_1.set_amplitude(self.a2)

    def get_a1(self):
        return self.a1

    def set_a1(self, a1):
        self.a1 = a1
        self.analog_sig_source_x_0.set_amplitude(self.a1)

    def get_a0(self):
        return self.a0

    def set_a0(self, a0):
        self.a0 = a0
        self.analog_sig_source_x_1.set_amplitude(self.a0)

    def get_Freq_fondamentale(self):
        return self.Freq_fondamentale

    def set_Freq_fondamentale(self, Freq_fondamentale):
        self.Freq_fondamentale = Freq_fondamentale
        self.analog_sig_source_x_0_1_0_1.set_frequency(5*self.Freq_fondamentale)
        self.analog_sig_source_x_0_1_0_0.set_frequency(4*self.Freq_fondamentale)
        self.analog_sig_source_x_0_1_0.set_frequency(3*self.Freq_fondamentale)
        self.analog_sig_source_x_0_1.set_frequency(2*self.Freq_fondamentale)
        self.analog_sig_source_x_0_0_0_0_1.set_frequency(5*self.Freq_fondamentale)
        self.analog_sig_source_x_0_0_0_0_0.set_frequency(4*self.Freq_fondamentale)
        self.analog_sig_source_x_0_0_0_0.set_frequency(3*self.Freq_fondamentale)
        self.analog_sig_source_x_0_0_0.set_frequency(2*self.Freq_fondamentale)
        self.analog_sig_source_x_0_0.set_frequency(self.Freq_fondamentale)
        self.analog_sig_source_x_0.set_frequency(self.Freq_fondamentale)


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
