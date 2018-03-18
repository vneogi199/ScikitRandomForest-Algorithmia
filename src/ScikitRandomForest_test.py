from . import ScikitRandomForest

def test_ScikitRandomForest():
    assert ScikitRandomForest.apply("Jane") == "hello Jane"
