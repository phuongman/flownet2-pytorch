#!/usr/bin/env python3
import os
import torch
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension  # Thay CUDAExtension bằng CppExtension

cxx_args = ['-std=c++11']  # Chỉ giữ các tham số C++ cần thiết

# Xóa nvcc_args vì không sử dụng CUDA

setup(
    name='channelnorm_cpu',  # Đổi tên để chỉ ra rằng đây là phiên bản chạy trên CPU
    ext_modules=[
        CppExtension('channelnorm_cpu', [  # Sử dụng CppExtension thay vì CUDAExtension
            #'channelnorm_cuda.cc',  # Loại bỏ các tệp CUDA
            'channelnorm_kernel.cpp'  # Chỉ sử dụng tệp C++ thay vì CUDA
        ], extra_compile_args={'cxx': cxx_args})  # Không cần nvcc_args nữa
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
