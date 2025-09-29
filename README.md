# PYTHON GAME
![Label](docs/label.png)

Приветик всем! Сегодня очень рад был видеть такое большое количество заинтересованных ребят, поэтому как и обещал скидываю вам гайдик по установке Python и VSCode.

## Python
Переходим по этой [ссылке](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe), у вас сразу же начнется скачивание. Далее вам требуется сделать несколько обязательных шагов, чтобы все работало корректно. Открывайте сам установщик и прожмите все как на картинках ниже:

### Шаг 1.

<img src="docs\installation\p1.png" alt="p1" width="400px">

### Шаг 2.

<img src="docs\installation\p2.png" alt="p2" width="400px">

### Шаг 3.

<img src="docs\installation\p3.png" alt="p3" width="400px">

Если все повторили как у меня, то все будет отлично и можно переходить к VSCode.

## VSCode
Переходите по данной [ссылке](https://code.visualstudio.com/) и жмите большую кнопку в середине экрана. 

<img src="docs\installation\v1.png" alt="v1" width="400px">

Дождитесь конца загрузки и открывайте установщик. Далее делаем все как на картинках:

### Шаг 1.

<img src="docs\installation\v2.png" alt="v2" width="400px">

### Шаг 2.

<img src="docs\installation\v3.png" alt="v3" width="400px">

### Шаг 3.

<img src="docs\installation\v4.png" alt="v4" width="400px">

## Настройка VSCode

Открываем VSCode. И сразу же переходим к установке расширений: 

<img src="docs\installation\vi1.png" alt="vi1" width="400px">

Найдите в открывшейся части поиск и напишите там Python:

<img src="docs\installation\vi2.png" alt="vi2" width="400px">
<img src="docs\installation\vi3.png" alt="vi3" width="400px">

Когда найдете расширение, то нажмите на него. Откроется вкладка, в которой нужно будет назвать на кнопку "Install":

<img src="docs\installation\vi4.png" alt="vi4" width="400px">

По своему желанию аналогично можете установить расширение с русским языком:

<img src="docs\installation\vi5.png" alt="vi5" width="400px">

## Создание проекта
Вернитесь на рабочий стол, создайте здесь папку (ПКМ > Создать > Новую папку) и переименуйте ее в "pygame"

Затем сделайте следующее действие (перетащите папку в VSCode):
![openPR](docs/openPROJECT.gif)

Откройте проводник в вашем проекте, если он все еще не открыт. И создайте новый файл main.py:

<img src="docs\exp_add.png" alt="exp_add" width="400px">

Вкладка с вашим файлом откроется автоматически, попробуйте написать `print("Hello, EasyCode")` и нажать на кнопку запуска:

<img src="docs\start.png" alt="start" width="400px">

## Установка PyGame

В открывшемся терминале напишите следующую команду и нажмите Enter:
```bash
pip install pygame
```
Теперь вам доступна возможность импорта библиотеки

```python
import pygame
```