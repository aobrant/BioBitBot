import os
from _decimal import Decimal
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.markdown import text
from itertools import cycle
import re

help_message = text(
    "/start",
    "/help",
    sep="\n"
)


class States(StatesGroup):
    home_state = State()
    weight_state = State()
    presure_state = State()
    walk_state = State()
    running_state = State()
    cycling_state = State()
    fitness_state = State()
    swimming_state = State()
    hiking_state = State()
    tennis_state = State()
    dlt_state = State()


def text_to_dec(txt):
    pattern = r'(\d{1,3}).*?(\d{1,3})'
    match = re.search(pattern, txt)
    if match:
        err = False
        number1 = int(match.group(1))
        number2 = int(match.group(2))
        number1_str = str(number1)
        number2_str = str(number2)
        combined_str = f"{number1_str}.{number2_str}"
        val = Decimal(combined_str)
    else:
        err = True
    return (val, err)


def dec_to_int(prsssure):
    number1 = []
    number2 = []
    pattern = r'(\d{1,3}).*?(\d{1,3})'
    for pr in prsssure:
        press_str = str(pr)
        match = re.search(pattern, press_str)
        number1.append(int(match.group(1)))
        number2.append(int(match.group(2)))
    return number1, number2


def plot_graph(user_id, name_par, units, dates, *parameter_list):
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))  # Форматирование оси даты и времени
    color_cycle = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])  # Используем цветовой цикл Matplotlib
    for i, parameter_values in enumerate(parameter_list):
        color = next(color_cycle)
        if name_par == 'blood_pressure':
            if i == 0:
                plt.plot(dates, parameter_values, marker='o', linestyle='-',
                         label=f'blood_pressure down', color=color)
            if i == 1:
                plt.plot(dates, parameter_values, marker='o', linestyle='-',
                         label=f'blood_pressure up  ', color=color)
        else:
            plt.plot(dates, parameter_values, marker='o', linestyle='-',
                     label=f'{name_par} {i + 1}', color=color)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel(f'{name_par} ({units})')
    plt.title(f'Graphs of {name_par} by date and time')
    plt.legend()
    plt.tight_layout()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    png_folder_path = os.path.join(current_directory, 'PNG')
    if not os.path.exists(png_folder_path):
        os.makedirs(png_folder_path)
    name1 = str(user_id)
    name2 = 'graph.png'
    name = '_'.join([name1, name2])
    file_path = os.path.join(png_folder_path, name)
    plt.savefig(file_path)
    return file_path


def counter_for_drinks_per_day(dates, parameters):
    date_dict = {}
    day_format = '%Y-%m-%d'
    for date, param in zip(dates, parameters):
        # day = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime(day_format)
        day = date.strftime(day_format)
        if day in date_dict:
            date_dict[day] += 1
        else:
            date_dict[day] = 1
    days = list(date_dict.keys())
    parameter_counts = list(date_dict.values())
    return days, parameter_counts


def plot_histogram(user_id, name_par, days, parameter_counts, units):
    plt.figure()
    plt.bar(days, parameter_counts)
    plt.xlabel('Days')
    plt.ylabel(f'number of ({units})')
    plt.title(f'Column histogram of {name_par} by day')
    plt.xticks(rotation=45)
    plt.tight_layout()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    png_folder_path = os.path.join(current_directory, 'PNG')
    if not os.path.exists(png_folder_path):
        os.makedirs(png_folder_path)
    name1 = str(user_id)
    name2 = 'graph.png'
    name = '_'.join([name1, name2])
    file_path = os.path.join(png_folder_path, name)
    plt.savefig(file_path)
    return file_path
