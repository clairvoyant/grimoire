

========
Contents
========

* json             :   data serializing using json.
* json-rpc         :   data serializing using json as remote call.
* multiprocessing  : example of multi processing using python.
* project          : basic project template with unit testing.
* twisted          : twisted network server/client.
* xml              : xml processing and chunk 


=================
GPU depdendencies
=================

    code-block:: bash
    conda create -n tensorflow-gpu python=3.9
    conda activate tensorflow-gpu
    conda install -c conda-forge tensorflow==2.7.0=cuda102*
