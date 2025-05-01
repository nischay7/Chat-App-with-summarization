FROM public.ecr.aws/lambda/python:3.10

COPY ./chat_app ${LAMBDA_TASK_ROOT}

COPY requirements.txt .
RUN pip3 install -r requirements.txt -t "${LAMBDA_TASK_ROOT}" -U --no-cache-dir

CMD ["main.handler"]

