# Tests for the CQCToFile class

# To get a temporary directory start the function with
#
# filename=os.path.join(tmpdir,'CQC_File')
#
# with CQCToFile(filename=filename) as cqc:



from cqc.pythonLib import CQCToFile, qubit
import os
from cqc.cqcHeader import CQC_TP_HELLO

def test_name(tmpdir):

    filename=os.path.join(tmpdir,'CQC_File')

    with CQCToFile(filename=filename) as cqc:
        assert cqc.name == 'CQCToFile'

def test_tempdir(tmpdir):

    filename=os.path.join(tmpdir,'CQC_File')

    with CQCToFile(filename=filename) as cqc:

        cqc.commit('test')        
        
        with open(filename) as f:
            contents = f.read()
            assert contents == 'test\n'

def test_sendSimple(tmpdir):

    filename=os.path.join(tmpdir,'CQC_File')

    with CQCToFile(filename=filename) as cqc:

        cqc.sendSimple(CQC_TP_HELLO)

        with open(filename) as f:
            contents = f.read()
            print(contents)
            assert contents[6:10] == "\\x00"

def test_createqubit(tmpdir):

    filename=os.path.join(tmpdir,'CQC_File')

    with CQCToFile(filename=filename) as cqc:

        q = qubit(cqc)

        with open(filename) as f:
            
            line = f.readline()
            print(line)

            assert line[6:10] == "\\x01"
            assert line[42:46] == "\\x01"