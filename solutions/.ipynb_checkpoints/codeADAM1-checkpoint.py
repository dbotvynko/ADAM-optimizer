{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "m_t = beta_1 * m_t + (1-beta_1) * batch_grad\n",
    "v_t = beta_2 * v_t + (1-beta_2) * np.square(batch_grad)\n",
    "\n",
    "m_t_hat = m_t / (1 - np.power(beta_1,i+1))\n",
    "v_t_hat = v_t / (1 - np.power(beta_2,i+1))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
