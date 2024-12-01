#!/usr/bin/env python3
import os
import torch
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension  # Thay CUDAExtension bằng CppExtension

cxx_args = ['-std=c++11']

# Loại bỏ phần nvcc_args liên quan đến CUDA
# nvcc_args không cần thiết nếu không dùng GPU

setup(
    name='resample2d_cpu',  # Đổi tên nếu cần
    ext_modules=[
        CppExtension('resample2d_cpu', [  # Chuyển sang sử dụng CppExtension
            #'resample2d_cuda.cc',  # Loại bỏ tệp CUDA
            'resample2d_kernel.cpp'  # Chỉ sử dụng tệp C++ thay vì tệp CUDA
        ], extra_compile_args={'cxx': cxx_args})  # Không cần nvcc_args nữa
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
