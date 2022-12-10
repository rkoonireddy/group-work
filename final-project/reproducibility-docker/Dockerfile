FROM python:latest

LABEL maintainer="Rohit Koonireddy <rohit13595@gmail.com>"

WORKDIR /usr/app/src.

#From python
RUN pip install --no-cache-dir --upgrade pip && \
    pip --no-cache-dir install numpy matplotlib pandas seaborn jupyterlab jupyter pandas_datareader datetime pyarrow fastparquet
EXPOSE 8888

#COPY ipynb files from relevant folder./
COPY Research_Final.ipynb ./

# Run app.py when the container launches
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]

#we should remember that docker should have the libraries needed