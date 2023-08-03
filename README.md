# Pathfinding-Visualizer
Pathfinding visualizer of the popular algorithms such as BFS, DFS, Dijkstra and A*. 
The algorithms implemented on backend which return visited nodes and path to the frontend to visualize them.

### Live demo [here](http://ec2-13-51-176-98.eu-north-1.compute.amazonaws.com)

---------------

## Built With
- [Python](https://www.python.org/) 3.6.x
- [Django Rest Framework](http://www.django-rest-framework.org/) 3.8.x
- [npm](https://www.npmjs.com) 8.5.x
- [React](https://react.dev) 16.13.x

## Usage

Clone this repository:

```shell
$ git clone git@github.com:cdoos/Pathfinding-Visualizer.git && cd Pathfinding-Visualizer
```
### Backend

Create new virtual environment:

```shell
$ python -m venv venv
```

Activate virtual environment:

```shell
$ source venv/bin/activate  (For Linux/Mac OS)
$ venv/Scripts/activate  (For Windows)
```

Install requirements:

```shell
$ pip install -r requirements.txt
```

Run the development server:

```shell
$ python manage.py runserver
```

### Frontend

Go to the frontend folder:
```shell
$ cd frontend
```

Install npm packages:
```shell
$ npm install
```

Run the development server:
```shell
$ npm start
```





