FROM public.ecr.aws/lambda/python:3.10
 
RUN pip install numpy==1.23.1
RUN pip install keras-image-helper
#RUN pip install tflite-runtime
RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp