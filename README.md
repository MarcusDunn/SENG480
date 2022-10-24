# SENG 480

This is the repository where our code is hosted to do data mining and analysis.

## Running Python

### Requirements

I can verify it works with the following environment, newer versions are likely fine, for older versions your mileage
may vary.

- Python 3.10.7
- pip 22.3

### Installing dependencies

I recommend using a [virtual environment](https://docs.python.org/3/library/venv.html).

Create the environment if it does not exist already

```bash
python3 -m venv venv
```

Enter the environment

```bash
source venv/bin/activate
```

Install the dependencies

```
pip install -r requirements.txt
```

### Running

Finally, you can run the script

```bash
python main.py
```