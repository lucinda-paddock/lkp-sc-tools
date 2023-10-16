import matplotlib
import seaborn as sns

def set_colors(items, colormap_name):
    '''
    Assign colors to items based on colormap.

    Parameters:
    items (iterable) - list of items
    colormap_name (str) - a seaborn supported colormap

    Returns:
    color_dict (dict) - dict containing item:color pairs
    '''
    color_dict = {}
    sns_colormap = sns.color_palette(colormap_name, len(items))
    for i, item in enumerate(items):
        color_dict[item] = sns_colormap[i]
    return color_dict

