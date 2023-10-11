SET var=%cd%
pip install -r requirements.txt
cd Backup\protobuf-python-3.18.1\protobuf-3.18.1\python
python setup.py build
python setup.py test
python setup.py install