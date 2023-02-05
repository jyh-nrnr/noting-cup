FROM amazon/aws-lambda-python:3.8

# WORKDIR /home/
# RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
# RUN apt-get update
# RUN apt-get install libgl1-mesa-glx
# RUN yum makecache --refresh
RUN yum -y install mesa-libGL-devel.x86_64

RUN yum install git -y

RUN git clone https://github.com/jyh-nrnr/noting-cup.git
# WORKDIR /home/noting-cup/
# RUN pip install -r noting-cup/requirements.txt
# COPY noting-cup/lambda_function.py ${LAMBDA_TASK_ROOT}
# COPY noting-cup/generate_image.py ${LAMBDA_TASK_ROOT}
# COPY noting-cup/notion_api.py ${LAMBDA_TASK_ROOT}
# COPY noting-cup/OTF/NanumSquareNeoOTF-aLt.otf ${LAMBDA_TASK_ROOT}
# COPY noting-cup/OTF/NanumSquareNeoOTF-bRg.otf ${LAMBDA_TASK_ROOT}
# COPY noting-cup/OTF/NanumSquareNeoOTF-cBd.otf ${LAMBDA_TASK_ROOT}
# COPY noting-cup/OTF/NanumSquareNeoOTF-dEb.otf ${LAMBDA_TASK_ROOT}
# COPY noting-cup/OTF/NanumSquareNeoOTF-eHv.otf ${LAMBDA_TASK_ROOT}
# COPY noting-cup/requirements.txt ${LAMBDA_TASK_ROOT}
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY generate_image.py ${LAMBDA_TASK_ROOT}
COPY notion_api.py ${LAMBDA_TASK_ROOT}
COPY OTF/NanumSquareNeoOTF-aLt.otf ${LAMBDA_TASK_ROOT}
COPY OTF/NanumSquareNeoOTF-bRg.otf ${LAMBDA_TASK_ROOT}
COPY OTF/NanumSquareNeoOTF-cBd.otf ${LAMBDA_TASK_ROOT}
COPY OTF/NanumSquareNeoOTF-dEb.otf ${LAMBDA_TASK_ROOT}
COPY OTF/NanumSquareNeoOTF-eHv.otf ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r noting-cup/requirements.txt --target "${LAMBDA_TASK_ROOT}"

# RUN cp noting-cup/lambda_function.py ${LAMBDA_TASK_ROOT}
# RUN cp noting-cup/generate_image.py ${LAMBDA_TASK_ROOT}
# RUN cp noting-cup/notion_api.py ${LAMBDA_TASK_ROOT}
# RUN cp noting-cup/OTF/NanumSquareNeoOTF-aLt.otf ${LAMBDA_TASK_ROOT}
# RUN cp noting-cup/OTF/NanumSquareNeoOTF-bRg.otf ${LAMBDA_TASK_ROOT}
# RUN cp noting-cup/OTF/NanumSquareNeoOTF-cBd.otf ${LAMBDA_TASK_ROOT}
# RUN cp noting-cup/OTF/NanumSquareNeoOTF-dEb.otf ${LAMBDA_TASK_ROOT}
# RUN cp noting-cup/OTF/NanumSquareNeoOTF-eHv.otf ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.handler"]

