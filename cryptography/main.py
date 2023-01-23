from project_1.project1 import start as start_project_1
from project_2.project2 import start as start_project_2
from project_3.project3 import start as start_project_3

if __name__ == '__main__':
    PROJECT_NUM = 3

    if PROJECT_NUM == 1:
        start_project_1()
    elif PROJECT_NUM == 2:
        start_project_2()
    elif PROJECT_NUM == 3:
        start_project_3()





