#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Extension
from distutils.sysconfig  import get_python_inc
import os

def get_vt_dirs(mode='seq'):
    
    from subprocess import PIPE, Popen 

    vt_library=[]
    vt_library_dirs=[]
    vt_include=[]

    p=Popen(['vtcc -vt:'+mode+' -vt:show'],shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE,close_fds=True)
    tmp = p.stdout.read().split()

    for item in tmp:
        if item[:2]=='-I':
            vt_include.append(item[2:])
        if item[:2]=='-L':
            vt_library_dirs.append(item[2:])   
        if item[:2]=='-l':
            vt_library.append(item[2:])
    
    return {'include_dirs':vt_include, 'library_dirs':vt_library_dirs, 'libraries':vt_library}


setup(name='VamPyTrace',
      version='0.1.0',
      description='Python Wrapper for VampirTrace',
      author='Christoph Statz',
      author_email='statz@wh2.tu-dresden.de',
      url='https://vampytrace.googlecode.com',
      packages=find_packages(),
      install_requires = ['mpi4py>=1.2.2'],
      include_package_data = True,
      license = "New BSD License",
      entry_points = {
        'console_scripts': [
            'vtpython = vampytrace:entry_point'
        ],
      },
      ext_modules=[
        Extension('vampytrace.instruments.seq._VT_User', ['src/vt_user.i'],
          swig_opts=['-DVTRACE', '-I'+get_python_inc(),'-I'+get_vt_dirs('seq')['include_dirs'][0]],
          include_dirs=[get_python_inc()]+get_vt_dirs('seq')['include_dirs'],
          library_dirs=get_vt_dirs('seq')['library_dirs'],
          libraries=get_vt_dirs('seq')['libraries'],
          define_macros=[('VTRACE',None)]
          ),
        Extension('vampytrace.instruments.mpi._VT_User', ['src/vt_user.i'],
          swig_opts=['-DVTRACE', '-I'+get_python_inc(),'-I'+get_vt_dirs('mpi')['include_dirs'][0]],
          include_dirs=[get_python_inc()]+get_vt_dirs('mpi')['include_dirs'],
          library_dirs=get_vt_dirs('mpi')['library_dirs'],
          libraries=get_vt_dirs('mpi')['libraries'],
          define_macros=[('VTRACE',None)]
          )
        Extension('vampytrace.instruments.mt._VT_User', ['src/vt_user.i'],
          swig_opts=['-DVTRACE', '-I'+get_python_inc(),'-I'+get_vt_dirs('mt')['include_dirs'][0]],
          include_dirs=[get_python_inc()]+get_vt_dirs('mt')['include_dirs'],
          library_dirs=get_vt_dirs('mt')['library_dirs'],
          libraries=get_vt_dirs('mt')['libraries'],
          define_macros=[('VTRACE',None)]
          )
        ]
     )
