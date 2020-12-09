FROM jupyter/pyspark-notebook:latest

EXPOSE 8888 8881

RUN conda install pandas
RUN conda install numpy
RUN conda install matplotlib
RUN conda install plotly
RUN conda install -c conda-forge nodejs
RUN conda update nodejs
RUN jupyter labextension install jupyterlab-plotly

COPY . .

