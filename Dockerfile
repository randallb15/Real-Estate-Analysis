FROM jupyter/pyspark-notebook:latest

EXPOSE 8888 8881

RUN conda install pandas
RUN conda install numpy
RUN conda install matplotlib
RUN conda install plotly

COPY . .

