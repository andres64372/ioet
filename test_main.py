import pytest
from main import main

def generate():
    examples = []
    example = ""
    inputs = []
    outputs = []
    line_type = "INPUT"
    with open('tests.txt','r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('Example'): 
            example = line.rstrip('\n')
        elif line.startswith('End'):
            examples.append((example,inputs,outputs))
            inputs = []
            outputs = []
            line_type = "INPUT"
        elif line.startswith('INPUT'): line_type = "INPUT"
        elif line.startswith('OUTPUT'): line_type = "OUTPUT"
        else:
            if not line == '\n':
                if line_type == "INPUT": inputs.append(line)
                if line_type == "OUTPUT": outputs.append(line.rstrip('\n'))
    return examples

@pytest.mark.parametrize("reference,test_input,expected", generate())
def test_eval(reference: str ,test_input: str, expected: str):
    output = main(test_input)
    assert output == expected, f"Error at {reference}"