from src.project_git_cheak.app import predict_price

def test_prediction():
    assert predict_price(1000) == 5000000