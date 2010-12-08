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


import vampytrace
from vampytrace.vampytraceconfig import VampyTraceConfig

def get_vt_version():
    from subprocess import PIPE, Popen 

    p=Popen(['vtcc -vt:version'],shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE,close_fds=True)
    vampirtrace_version = p.stdout.read()[:-1]
    vampirtrace_version = vampirtrace_version + ', VamPyTrace-'+str(vampytrace.__version__)	    
    return vampirtrace_version



class VampyTraceClParser():
    def __init__(self):

        import argparse

        parser = argparse.ArgumentParser(
            prog="vtpython",
	    formatter_class = argparse.RawDescriptionHelpFormatter,
            description='vtpython\n - A Python wrapper for VampirTrace',
            add_help=False,
            epilog = """\

environment variables:
  VT_INST               Instrumentation type (equivalent to '-vt:inst'*)
  VT_CC                 C compiler command (equivalent to '-vt:cc '*)
  VT_CFLAGS             C compiler flags
  VT_LDFLAGS            Linker flags
  VT_LIBS               Libraries to pass to the linker

* The corresponding command line options overwrites the environment variables setting.

examples:
  automatically instrumentation:

  vtpython -vt:cc gcc -vt:inst automatic example.py

  manually instrumentation by using VT's API:

  vtpython -vt:inst manual example.py

\n
"""
        )


        parser.add_argument(
            '-vt:help', 
            action='help', 
            default=argparse.SUPPRESS,
            help=('Show this help message.'))

        parser.add_argument(
            '-vt:version',
            action='version',
            default=argparse.SUPPRESS,
            version=get_vt_version(),
            help=("Show VampirTrace and VamPyrTrace version."))

        parser.add_argument(
	    '-vt:cc',
            type=str,
            dest='vtcc',
            help=('Set the underlying compiler command.'))  

        parser.add_argument(
	    '-vt:inst',
            type=str,
            dest='vtinst',
            default='compinst',
            choices=('compinst','manual'),
            help=('Set the instrumentation type'))

        parser.add_argument(
	    '-vt:pyinst',
            type=str,
            dest='pyinst',
            default='automatic',
            choices=('automatic','manual'),
            help=('Set the Python instrumentation type.'))  

        parser.add_argument(
	    '-vt:mpi',
            dest='mpi',
            action='store_true',
            help=('Enable tracing of MPI parallel code.'))  

        parser.add_argument(
	    '-vt:mt',
            dest='mt',
            action='store_true',
            help=('Enable tracing of multithreaded code.'))  

        parser.add_argument(
            'file',
            help=('Python script to be parsed.'))

        self.parser = parser

    def parse(self, args):
        
        values = self.parser.parse_known_args(args)
        config = VampyTraceConfig(values)
        
        return config, values[1]
