import numpy as np

import lab2.given_func as given


def grad_desc_with_const_lr(x_start, y_start, learning_rate, precision):
    iteration = 0
    print(
        f"iteration: {iteration}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
    iteration += 1

    points = np.array([x_start, y_start])
    while True:
        x_start = x_start - learning_rate * given.df_x(x_start, y_start)
        y_start = y_start - learning_rate * given.df_y(x_start, y_start)
        points = np.append(points, [x_start, y_start])

        print(f"iteration: {iteration}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
        iteration += 1

        if np.abs(given.df_x(x_start, y_start)) <= precision and np.abs(given.df_y(x_start, y_start)) <= precision:
            break

    return points
