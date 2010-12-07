# -*- coding: utf-8 -*-

""" VamPyTrace - A VampirTrace Wrapper in Python """

__copyright__ = "Copyright (c) 2010, Christoph Statz"

__license__ = """
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions 
are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS 
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import sys
import vampytrace


class VampyTrace():

    def __init__(self, instruments):
        self.instruments=instruments

    def trace(self, frame, event, arg):
       
        code = frame.f_code
        function_name = code.co_name
        function_file_name = code.co_filename
        function_linenumber = frame.f_lineno
        if event=='return':
            self.instruments.VT_User_end(function_name)
            return
        elif event=='call':
            self.instruments.VT_User_start(function_name,function_file_name,function_linenumber)
            return self.trace	


def main():

    parser = vampytrace.VampyTraceClParser()
    vtc, argv = parser.parse(sys.argv)

    import imp
    
    instruments = __import__('vampytrace.instruments.'+vtc.mode, fromlist=['vampytrace.instruments'])
    tracer = VampyTrace(instruments)

    sys.settrace(tracer.trace)

    instruments.VT_User_trace_on()
    probe = imp.load_source('probe',argv[0])
    instruments.VT_User_trace_off()

    try:
        instruments.VT_User_trace_on()
        probe.main()
        instruments.VT_User_trace_off()
    except AttributeError:
        pass

