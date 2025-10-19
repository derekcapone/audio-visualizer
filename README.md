Tested on Python 3.12, should have at least Python 3.9.


Setup Process:
1. Install OpenGL by using the following commands (Ubuntu/Linux only):

- Run this command:<br>
`sudo apt install mesa-utils`

Then verify using `glxinfo | grep "OpenGL version"`

- Then run the following command:<br>
`sudo apt install libglu1-mesa-dev freeglut3-dev mesa-common-dev`

2. Generate a virtual environment by running the following command:<br>
`python3 -m venv .venv`

Then activate the virtual environment with the following command:<br>
`source .venv/bin/activate`

3. Install pip packages using the following command in the project root folder:<br>
`pip install -r requirements.txt`

