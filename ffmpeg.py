#!/usr/bin/python

import os

args = [
    'extra-cflags="-c -Oz -fPIC -msse -msse2 -msse3 -msimd128 -pthread"',
    'extra-cxxflags="-msse -msse2 -msse3 -msimd128 -pthread"',
    'cc=emcc',
    'cxx=em++',
    'ar=emar',
    'ranlib=emranlib',
    'prefix=../wasm/obj',
    'target-os=none',
    'arch=x86_64',
    'cpu=generic'
    ]
disables = [
    'everything','all','avdevice','postproc','avfilter','programs','asm','parsers','muxers','demuxers','filters',
    'doc','devices','network','bsfs','shared','hwaccels','debug','protocols','indevs','outdevs','runtime-cpudetect'
]
enables = [
    'small','cross-compile','gpl','avcodec','swresample','ffmpeg','avformat',
    'muxer=mp4',
    'parser=h264',
    'parser=hevc',
    'parser=aac',
    'decoder=h264',
    'decoder=hevc',
    'decoder=aac',
    'decoder=pcm_alaw',
    'decoder=pcm_mulaw',
    'encoder=pcm_alaw',
    'encoder=pcm_mulaw',
    'encoder=aac','static','pthreads'
]
enables = ['enable-'+item for i,item in enumerate(enables)]
disables = ['disable-'+item for i,item in enumerate(disables)]
os.system('emconfigure ./configure --' +
          (' --'.join(args+disables+enables)))
os.system('make clean && emmake make -j && make install')
