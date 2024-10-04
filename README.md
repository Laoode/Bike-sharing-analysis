# 📊📈🚲 USA Bikes Sharing Data
## Overview
<p>Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return 
back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return 
back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of 
over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, 
environmental and health issues.</p>

<p>Apart from interesting real world applications of bike sharing systems, the characteristics of data being generated by
these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration
of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into
a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important
events in the city could be detected via monitoring these data.</p>

<p>The app was developed as a Data Analysis Project using the [Bike Sharing Dataset (Source)](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing).</p>

<p>A live version of the application can be found on Streamlit Community Cloud.</p>

## Installation
<p>You can run this inside a virtual environment to make it easier to manage dependencies. I recommend using `conda` to create a new environment and install the required packages. You can create a new environment called `bike-sharing-analysis` by running:</p>

`conda create -n bike-sharing-analysis python=3.11` 
<p>Then, activate the environment:</p>

`conda activate bike-sharing-analysis`
<p>To install the required packages, run:</p>

`pip install -r requirements.txt`
<p>This will install all the necessary dependencies, including Streamlit, pandas, seaborn, matplotlib</p>

## Usage
<p>To start the app, simply run the following command:</p>

`streamlit run app/main.py`
<p>After running the command, Streamlit will automatically launch the app in your default web browser.</p>