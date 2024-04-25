import econpizza as ep
import matplotlib.pyplot as plt
import numpy as np

def test_shock(var_shock, model):

    shk = (var_shock, 0.01 ** 2)
    x, flag = model.find_path(shock=shk)
    return x

def plot_results(num_simuls, model, x):

    num_rows = int(np.ceil(len(model['variables']) / 3))

    fig, axs = plt.subplots(num_rows, 3, figsize=(10, 4))
    for i, v in enumerate(()):
        axs.flatten()[i].plot(x[:num_simuls, model['variables']])
        axs.flatten()[i].set_xlabel(v)
    
    plt.show()

def read_model(yaml_name: str):
    model = ep.load(yaml_name,
                    raise_errors=True,
                    verbose=True)
    return model