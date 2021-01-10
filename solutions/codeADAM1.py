m_t = beta_1 * m_t + (1-beta_1) * batch_grad
v_t = beta_2 * v_t + (1-beta_2) * np.square(batch_grad)
m_t_hat = m_t / (1 - np.power(beta_1,i+1))
v_t_hat = v_t / (1 - np.power(beta_2,i+1))