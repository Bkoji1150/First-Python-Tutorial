FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}
COPY s3_accessor.py ${LAMBDA_TASK_ROOT}
COPY dynamoDb_accessor.py ${LAMBDA_TASK_ROOT}

# Run pip install to install dependencies
RUN pip install requests \
		pandas

# Set the CMD to your handler
CMD [ "app.handler" ]