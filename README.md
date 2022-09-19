# Estimate Pi with Montecarlo

## Introduction 
Estimating the value of Pi $\pi$ with the Monte Carlo method is a common algorithm in computer science.

The idea of this algorithm is take a great number of random points in a square of side $2r$ centered on (0,0). Then put a circle with radius $r$ inscribed into the square. With that calculate the ratio of number points that lied inside the circle and total number of random points generated.

We know the area of the square is $4r^{2}$ and the area of circle is $\pi r^{2}$.  
So the ratio of these two areas is:


$$ \frac{\pi r^{2}}{4r^{2}} = \frac{\text{area of the circle}}{\text{area of the square}} = \frac{\pi}{4} $$


Now if we take a large number of random points to represent the area of this both figures:

$$ \frac{\pi}{4} = \frac{N^\circ \text{points inside of the circle}}{\text{Total $N^\circ$ points}}$$

Finally:

$$ \pi = 4 * \frac{ N^\circ \text{points inside of the circle}}{\text{Total $N^\circ$ points}}$$


## Code

In this example exist three implementations of the algorithm, pure python, numba and numpy implementation.

In order to run the examples first you have to install requirements.

```bash
pip install -r requirements.txt
```

Then you can run the main file to get the execution time of the methods.

```bash
python main.py
```
