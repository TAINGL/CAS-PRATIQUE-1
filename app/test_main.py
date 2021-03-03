from fastapi.testclient import TestClient

from main import app
goodtoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
badtoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6Ikp"
client = TestClient(app)

def test_get():
    response = client.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"message" : "Bonjour, ceci est la beta d'un algorithm d'analyse de sentiment"}

def test_post_bad_token():
    response = client.post("/sentiment",
                            headers={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6Ikp"}, json={"text":"J'aime cette glace!"})
    #response = client.post("/sentiment",
    #                        headers={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6Ikp"}, json={"text":"J'aime cette glace!"})
    assert response.status_code == 401
    assert response.json() == {"message" : "Token Invalide"}

def test_post_empty_text():
    response = client.post("/sentiment",
                            headers={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"}, json={"text":None})
    assert response.status_code == 400
    assert response.json() == {"message": "Write your text or more than 3 caracteres"}

def test_post_good_prediction():
    response = client.post("/sentiment",
                            headers={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"}, json={"text":"J'adore cette glace"})
    assert response.status_code == 200
    assert response.json() == {
                                "text" : "J'adore cette glace",
                                "prediction" : "Positif"
                              }

def test_post_bad_prediction():
    response = client.post("/sentiment",
                            headers={"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"}, json={"text":"C'est l'horreur. Je ne reviendrais plus jamais ici!"})
    assert response.status_code == 200
    assert response.json() == {
                                "text" : "C'est l'horreur. Je ne reviendrais plus jamais ici!",
                                "prediction" : "Négatif"
                              }


