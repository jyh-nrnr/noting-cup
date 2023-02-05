FROM amazon/aws-lambda-python:3.8

# RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

RUN yum install git -y

RUN git clone https://github.com/jyh-nrnr/noting-cup.git

RUN pip install -r noting-cup/requirements.txt

# RUN cd noting-cup
RUN cp noting-cup/lambda_function.py /var/task/
RUN cp noting-cup/generate_image.py /var/task/
RUN cp noting-cup/notion_api.py /var/task/
RUN cp noting-cup/OTF/NanumSquareNeoOTF-aLt.otf /var/task/
RUN cp noting-cup/OTF/NanumSquareNeoOTF-bRg.otf /var/task/
RUN cp noting-cup/OTF/NanumSquareNeoOTF-cBd.otf /var/task/
RUN cp noting-cup/OTF/NanumSquareNeoOTF-dEb.otf /var/task/
RUN cp noting-cup/OTF/NanumSquareNeoOTF-eHv.otf /var/task/

CMD ["lambda_function.handler"]

