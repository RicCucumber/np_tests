"""
Обход дерева (поиск по дереву) с помощью Python­­-рекурсии
1. Реализуйте класс: Node, который будет использоваться для представления дерева
   У каждого узла (Node) есть имя и потомки
2. Выведите все пути к дереву, которые приведут вас в узел под названием Goal.
3. Дерево может состоять из N уровней (1>N>100), а узел Goal может содержать потомков.
"""
class Node:
    #Контейнер для хранения пройденных узлов
    path = []
    #Контейнер правильных путей
    result = []
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def find_path(self, goal):
        #Добавляем в контейнер текущий узел
        self.path.append(self.name)
        #Добавление текущего состояния контейнера в контейнер результатов
        if self.name == goal:
            self.result.append(' -> '.join(self.path))
        #Рекурсия поиска для потомков узла
        for child in self.children:
            child.find_path(goal)
        #Удаление узла из контейнера после прохождения по всем потомкам
        self.path.remove(self.name)

        return self.result
