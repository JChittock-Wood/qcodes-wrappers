# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:09:14 2017

@author: diepencjv
"""

#%%
from qcodes import Instrument
from qcodes.utils.validators import Numbers
from qcodes.instrument.parameter import ManualParameter

#%%


class hardware(Instrument):

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

        awg_gates = ['P1', 'P2', 'P3', 'P4']
        for gate in awg_gates:
            p = 'awg_to_%s' % gate
            self.add_parameter(p, parameter_class=ManualParameter,
                               initial_value=0,
                               label='{} (factor)'.format(p),
                               vals=Numbers(0, 400))

        # marker channels
        for gate in ['m4i_mk', 'awg_mk']:
            p = 'awg_to_%s' % gate
            self.add_parameter(p, get_cmd=None, initial_value=1, set_cmd=None)

        filterboxes = [1, 2, 3]
        for boxnum in filterboxes:
            p = 'filterbox_%d' % boxnum
            self.add_parameter(p, parameter_class=ManualParameter,
                               initial_value=0,
                               label='{} (frequency)'.format(p),
                               unit='Hz',
                               vals=Numbers(0, 500e3))

        p = 'delay_AWG'
        self.add_parameter(p, parameter_class=ManualParameter,
                           initial_value=0,
                           label='{} (time)'.format(p),
                           unit='s',
                           vals=Numbers(0, 1))

    def get_idn(self):
        ''' Overrule because the default VISA command does not work '''
        IDN = {'vendor': 'QuTech', 'model': 'hardwareV2',
               'serial': None, 'firmware': None}
        return IDN

