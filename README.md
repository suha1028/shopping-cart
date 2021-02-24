# Shopping Cart

# Software needed
You should already have: Anaconda 3.7+ Python 3.7+ Pip

# Installation
To begin, fork this remote repository and then clone/download it onto your own desktop. Then, please naviagte to command-line/terminal. 

```sh
cd ~/Desktop/shopping-cart
```
Then, use Anaconda to create a virtual environment called "shopping-env"

```sh
conda create -n shopping-env python = 3.8
conda activate shopping-env
```

From the virtual environment, install this package dependency:

```sh
pip install -r requirements.txt
```
# Setup
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired tax rate":

```sh
TAX_RATE = 0.0875
```

# Running the application: 
```sh
python shopping_cart.py
```
Please follow the instructions and enjoy!
