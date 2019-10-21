# Tests for the CQCToFile class

# To get a temporary directory start the function with
#
# filename=os.path.join(tmpdir,'CQC_File')
#
# with CQCToFile(filename=filename) as cqc:



from cqc.pythonLib import CQCToFile, qubit
import os

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
