# tortoise-assignment

## How to install


## Introduction
This repo contains assignment given by tortoise.pro.
1. Run `pip3 install -r requirement.txt`
2. Create migrations: `python3 manage.py makemigrations`
3. Make migrations: `python3 manage.py migrate`
4. Use postman collection to make API requests.
## Endpoints

### API Endpoints:

These are the available API endpoints with there respective functionality.
plans/plans/
plans/plan/
plans/planById
user/goals/
user/goal/
promotion/promotions/
promotion/promotion/ 

| Method   | URL                                      | Description                                                  |
| -------- | ---------------------------------------- | -------------------------------------------------------------|
| `GET`    | `plans/plans/`                           | Retrieve all available plans with promotional offer info.    |
| `POST`   | `plans/plan/`                            | Create a new Plan.                       |
| `GET`    | `plans/planById`                         | Retrieve plan by given plan ID                     |
| `GET`  | `user/goals/`                          | Retrieve all the user goals, provided userId.                 |
| `POST`   | `user/goal/`                 | Create user goals.                 |
| `GET`    | `promotion/promotions/` | Fetch all the available promotional offers. |
| `POST` | `promotion/promotion/ `| Create promotions endpoint.                    |
