# Prosta aplikacja do zarządzania użytkownikami (User Management API)

Prosta aplikacja backendowa demonstrująca wykorzystanie kontrolerów, obsługę żądań HTTP oraz podstawowe operacje CRUD (Create, Read, Update, Delete).

## 📚 Funkcjonalności

- Implementacja kontrolera obsługującego żądania HTTP
- Zarządzanie użytkownikami: dodawanie, wyświetlanie, edycja, usuwanie
- Walidacja danych przy dodawaniu nowych użytkowników
- Interfejs Swagger UI do testowania endpointów

## 🚀 Endpointy API

| Metoda | Endpoint          | Opis                                    |
|--------|-------------------|-----------------------------------------|
| GET    | `/users`          | Pobierz listę wszystkich użytkowników   |
| POST   | `/users`          | Dodaj nowego użytkownika (z walidacją)  |
| GET    | `/users/{id}`     | Pobierz dane użytkownika po ID          |
| PUT    | `/users/{id}`     | Zaktualizuj dane użytkownika po ID      |
| DELETE | `/users/{id}`     | Usuń użytkownika po ID                  |

## 🛠 Uruchamianie aplikacji

Upewnij się, że masz zainstalowanego Pythona. Następnie uruchom aplikację poleceniem:

```bash
python swagger.py





