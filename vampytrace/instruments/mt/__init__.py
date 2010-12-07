# -*- coding: utf-8 -*-

""" VamPyTrace - A VamtrTrace Wrapper in Python """

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

from vampytrace.instruments.mt.VT_User import VT_User_is_trace_on__ as VT_User_is_trace_on
from vampytrace.instruments.mt.VT_User import VT_User_trace_on__ as VT_User_trace_on
from vampytrace.instruments.mt.VT_User import VT_User_trace_off__ as VT_User_trace_off
from vampytrace.instruments.mt.VT_User import VT_User_buffer_flush__ as VT_User_buffer_flush
from vampytrace.instruments.mt.VT_User import VT_User_timesync__ as VT_User_timesync
from vampytrace.instruments.mt.VT_User import VT_User_update_counter__ as VT_User_update_counter
from vampytrace.instruments.mt.VT_User import VT_User_set_rewind_mark__ as VT_User_set_rewind_mark
from vampytrace.instruments.mt.VT_User import VT_User_rewind__ as VT_User_rewind
from vampytrace.instruments.mt.VT_User import VT_User_comment_def__ as VT_User_comment_def
from vampytrace.instruments.mt.VT_User import VT_User_comment__ as VT_User_comment
from vampytrace.instruments.mt.VT_User import VT_User_marker_def__ as VT_User_marker_def
from vampytrace.instruments.mt.VT_User import VT_User_count_group_def__ as VT_User_group_def
from vampytrace.instruments.mt.VT_User import VT_User_count_def__ as VT_User_count_def
from vampytrace.instruments.mt.VT_User import VT_User_count_signed_val__ as VT_User_count_signed_val
from vampytrace.instruments.mt.VT_User import VT_User_count_unsigned_val__ as VT_User_count_unsigned_val
from vampytrace.instruments.mt.VT_User import VT_User_count_float_val__ as VT_User_count_float_val
from vampytrace.instruments.mt.VT_User import VT_User_count_double_val__ as VT_User_count_double_val
from vampytrace.instruments.mt.VT_User import VT_User_marker__ as VT_User_marker
from vampytrace.instruments.mt.VT_User import VT_User_start__ as VT_User_start
from vampytrace.instruments.mt.VT_User import VT_User_end__ as VT_User_end

from vampytrace.instruments.mt.VT_User import VT_COUNT_DEFGROUP
from vampytrace.instruments.mt.VT_User import VT_COUNT_TYPE_SIGNED
from vampytrace.instruments.mt.VT_User import VT_COUNT_TYPE_UNSIGNED
from vampytrace.instruments.mt.VT_User import VT_COUNT_TYPE_FLOAT
from vampytrace.instruments.mt.VT_User import VT_COUNT_TYPE_DOUBLE
from vampytrace.instruments.mt.VT_User import VT_COUNT_TYPE_INTEGER
from vampytrace.instruments.mt.VT_User import VT_COUNT_TYPE_INTEGER8
from vampytrace.instruments.mt.VT_User import VT_COUNT_TYPE_REAL
from vampytrace.instruments.mt.VT_User import VT_MARKER_TYPE_ERROR
from vampytrace.instruments.mt.VT_User import VT_MARKER_TYPE_WARNING
from vampytrace.instruments.mt.VT_User import VT_MARKER_TYPE_HINT
