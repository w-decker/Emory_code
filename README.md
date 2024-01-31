# Emory_code

## Dependencies

#### These plots rely on `nilearn.plotting()`, `matplotlib.pyplot()`and `matplotlib.animation.FuncAnimation()`.

## Making the plots

#### To generate the brain plots, clone this repository

```bash
git clone https://github.com/w-decker/Emory_code.git
```

#### Next, add a config.py file with a specified directory to save your images.

```bash
touch config.py | echo "IMAGE_DIR = '/path/to/dir' " >> config.py
```

#### To execute the file in the terminal, run the following.

```bash
python3.12 main.py
```
