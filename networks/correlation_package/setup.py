#!/usr/bin/env python3
import os
import torch
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension  # Thay CUDAExtension bằng CppExtension

cxx_args = ['-std=c++11']

# Xóa nvcc_args vì không sử dụng CUDA

setup(
    name='correlation_cpu',  # Đổi tên nếu cần
    ext_modules=[
        CppExtension('correlation_cpu', [  # Chuyển sang sử dụng CppExtension
            #'correlation_cuda.cc',  # Loại bỏ tệp CUDA
            'correlation_cuda_kernel.cpp'  # Sử dụng tệp C++ thay vì tệp CUDA
        ], extra_compile_args={'cxx': cxx_args})  # Không cần nvcc_args nữa
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
