# markdown-preview-enhanced-python-example

## Setup

You need to have already installed all the litvis extensions as per the instructions [here](https://github.com/gicentre/litvis)

To use this template first you need to make a virtual python environment, this is to guarantee that it uses python 3 and has the required modules: 
```
python3 -m pip install virtualenv
```

Then you need to make a virtual python environment in the root directory of your project:
```
virtualenv venv
```

Set your shell to use this version of python for that shell session (will have to be done each time you reopen the project):
```
source venv/bin/activate
```

Now you can install altair in this new virtual python environment (and any other packages you may want):
```
pip install altair numpy pandas
```

Now put all the packages in a `requirements.txt` so that anyone else can install the necessary packages to run your project with `pip install -r requirements.txt`:
```
pip freeze > requirements.txt
```

## How to Use

To make a new visualisation copy the example 
```
cp python/altair_example.py python/new_visualisation.py
```

Then open new visualisation and **place your code to produce the visualisation in the `visualisation()` function**. This function **must return an altair object**

Generate a vega-lite file by running this in the root project folder:
```
./generate_vis
```

you **may** get a permissions error in which case do this then try again:
```
chmod +x generate_vis
chmod +x python/*
```

This will generate vega visualisations and place them in the `/vega` folder

now you can view the code by importing the file as a code block using `line_begin` and `line_end` tags to cut out the boilerplate:

@import "python/altair_example.py" {line_begin=4 line_end=21}

You can observe the visualisation by importing the vega-lite json like so:

@import "vega/altair_example.json" {as="vega-lite"}

Now if you change any of your python scripts you update the vega-lite json by:
```
./generate_vis
```