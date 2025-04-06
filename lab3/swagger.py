from flask import Flask, jsonify, request, abort
from flasgger import Swagger
import random
import string

app = Flask(__name__)
Swagger(app)  #Swagger UI do aplikacji

# Lista przykładowych użytkowników
users = [
    {"id": "1", "name": "Jan Kopeć", "email": "jan.kopec@gmail.com"},
    {"id": "2", "name": "Elon Musk", "email": "elon.musk@x.com"},
    {"id": "3", "name": "Olaf Papuga", "email": "papuga@gmail.com"},
    {"id": "4", "name": "Julia Śliwa", "email": "julia.sliwa@gmail.com"},
    {"id": "5", "name": "Adam Kojder", "email": "adam.kojder@gmail.com"},
    {"id": "6", "name": "Maksymilian Nowak", "email": "maks.nowak@gmail.com"},
    {"id": "7", "name": "Piotr Kowalski", "email": "piotr.kowalski@gmail.com"},
    {"id": "8", "name": "Magdalena Wiśniewska", "email": "magdalena.wisniewska@gmail.com"},
    {"id": "9", "name": "Robert Lewandowski", "email": "robert.lewandowski@gmail.com"},
    {"id": "10", "name": "Agnieszka Zielińska", "email": "agnieszka.zielinska@gmail.com"}
]

# Funkcja do walidacji e-maila
def is_valid_email(email):
    return '@' in email and '.' in email

# Funkcja do walidacji imienia
def is_valid_name(name):
    return len(name) >= 3

# Funkcja do generowania unikalnych ID
def generate_unique_id():
    return ''.join(random.choices(string.digits, k=5))

# Endpoint GET /users
@app.route("/users", methods=["GET"])
def get_users():
    """
    Endpoint do pobierania użytkowników.
    ---
    parameters:
      - name: limit
        in: query
        type: integer
        default: 10
      - name: offset
        in: query
        type: integer
        default: 0
      - name: name
        in: query
        type: string
    responses:
      200:
        description: Lista użytkowników
        schema:
          type: array
          items:
            properties:
              id:
                type: string
              name:
                type: string
              email:
                type: string
    """
    limit = request.args.get("limit", default=10, type=int)
    offset = request.args.get("offset", default=0, type=int)
    name_filter = request.args.get("name", default="", type=str)

    # Filtrowanie po nazwie
    filtered_users = [user for user in users if name_filter.lower() in user["name"].lower()]

    # Paginacja
    paginated_users = filtered_users[offset:offset+limit]

    return jsonify(paginated_users)

# Endpoint POST /users
@app.route("/users", methods=["POST"])
def create_user():
    """
    Endpoint do tworzenia nowego użytkownika.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Olga Nowak"
            email:
              type: string
              example: "olga.nowak@gmail.com"
    responses:
      201:
        description: Utworzony użytkownik
        schema:
          id: User
          properties:
            id:
              type: string
            name:
              type: string
            email:
              type: string
    """
    data = request.get_json()

    # Walidacja danych
    if not data.get("name") or not is_valid_name(data["name"]):
        abort(400, description="Imię musi mieć co najmniej 3 znaki")
    if not data.get("email") or not is_valid_email(data["email"]):
        abort(400, description="Nieprawidłowy adres e-mail")

    # Tworzenie nowego ID
    new_id = generate_unique_id()
    user = {"id": new_id, "name": data["name"], "email": data["email"]}
    users.append(user)

    return jsonify(user), 201

# Endpoint GET /users/{id}
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """
    Endpoint do pobierania użytkownika po ID.
    ---
    parameters:
      - name: user_id
        in: path
        type: string
    responses:
      200:
        description: Szczegóły użytkownika
        schema:
          id: User
          properties:
            id:
              type: string
            name:
              type: string
            email:
              type: string
      404:
        description: Użytkownik nie znaleziony
    """
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        abort(404, description="Użytkownik nie znaleziony")
    return jsonify(user)

# Endpoint PUT /users/{id}
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Endpoint do aktualizacji użytkownika po ID.
    ---
    parameters:
      - name: user_id
        in: path
        type: string
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: Zaktualizowany użytkownik
        schema:
          id: User
          properties:
            id:
              type: string
            name:
              type: string
            email:
              type: string
      400:
        description: Nieprawidłowe dane
      404:
        description: Użytkownik nie znaleziony
    """
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        abort(404, description="Użytkownik nie znaleziony")

    data = request.get_json()

    # Walidacja danych
    if not data.get("name") or not is_valid_name(data["name"]):
        abort(400, description="Imię musi mieć co najmniej 3 znaki")
    if not data.get("email") or not is_valid_email(data["email"]):
        abort(400, description="Nieprawidłowy adres e-mail")

    # Aktualizacja użytkownika
    user["name"] = data["name"]
    user["email"] = data["email"]

    return jsonify(user)

# Endpoint DELETE /users/{id}
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Endpoint do usuwania użytkownika po ID.
    ---
    parameters:
      - name: user_id
        in: path
        type: string
    responses:
      204:
        description: Użytkownik usunięty
      404:
        description: Użytkownik nie znaleziony
    """
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        abort(404, description="Użytkownik nie znaleziony")

    users.remove(user)
    return '', 204  # Brak treści dla usuniętego użytkownika

# Obsługa błędów
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": error.description, "status": 400}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": error.description, "status": 404}), 404

if __name__ == "__main__":
    app.run(debug=True)
