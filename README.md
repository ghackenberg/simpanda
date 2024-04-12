# SimPy + Panda3D Boilerplate

![](./images/social_preview.png)

This project contains **boilerplate code** for combined **discrete event simulation (DES)** and **hardware-accelerated 3D visualization** with ...

- the **Python** programming language,
- the **SimPy** discrete event simulation library, and
- the **Panda3D** visulization framework.

We use the boilerplate code at the [School of Engineering](https://fh-ooe.at/campus-wels) of the [University of Applied Sciences Upper Austria](https://fh-ooe.at/) in courses on **computer simulation** and **digital factory**.

## 🖼️ Screenshots

![](./images/screenshot.png)

## ⚙️ Requirements

### SimPy

SimPy provides **discrete event simulation capabilities** for Python programs.

```sh
pip install simpy
```

### Panda3D

Panda3D provides **hardware-accelerated 3D visualization capabilities** for Python programs.

```sh
pip install panda3d
```

## 🧑‍💻 Snippets

```python
from simpanda import Container
from simpanda import cubeNodePath

# Create container including simulation environment and visualization window
container = Container(1, 10)

# Create cube geometry and attach it to visualization window
cubeNodePath().reparentTo(container.app.render)

# Start simulation and visualization threads
container.run()
```

## 📁 Folders

* [Images](./images/)
* [Sources](./sources/)

## 📄 Documents

* [License](./LICENSE.md)
* [Changelog](./CHANGELOG.md)
* [Contributing](./CONTRIBUTING.md)