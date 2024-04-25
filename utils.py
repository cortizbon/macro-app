import econpizza as ep
import matplotlib.pyplot as plt
import numpy as np

def test_shock(var_shock, model):

    shk = (var_shock, 0.01 ** 2)
    x, flag = model.find_path(shock=shk)
    return x

def plot_results(num_simuls, model, x):

    num_rows = int(np.ceil(len(model['variables']) / 3))

    fig, axs = plt.subplots(num_rows, 3, figsize=(8, 4))
    for i, v in enumerate(model['variables']):
        axs.flatten()[i].plot(x[:num_simuls, model['variables'].index(v)])
        axs.flatten()[i].set_xlabel(v)
        axs.flatten()[i].spines['top'].set_visible(False)
        axs.flatten()[i].spines['right'].set_visible(False)
    
    fig.tight_layout()
    return fig

def read_model(yaml_name: str):
    model = ep.load(yaml_name,
                    raise_errors=True,
                    verbose=True)
    return model

def check_if_list(val):
    if not isinstance(val, list):
       raise ValueError 
    
def sensitivity_analysis(val, param, var_shock, model, num_simuls=50):

    num_rows = int(np.ceil(len(model['variables']) / 3))
    fig, axs = plt.subplots(num_rows, 3, figsize=(8, 4))
    for elem in val:
        model['steady_state']['fixed_values'][param] = elem
        _ = model.find_stst()
        shk = (var_shock, 0.01 ** 2)
        x, flag = model.find_path(shock=shk)
        
        for i, v in enumerate(model['variables']):
            axs.flatten()[i].plot(x[:num_simuls, model['variables'].index(v)])
            axs.flatten()[i].set_xlabel(v)
            axs.flatten()[i].spines['top'].set_visible(False)
            axs.flatten()[i].spines['right'].set_visible(False)
    fig.tight_layout()
    return fig
        

