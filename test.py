import jax, jax.numpy as jnp
print(jax.devices())
x = jnp.ones((64, 19, 11, 11))
k = jnp.ones((32, 19, 5, 5))
y = jax.lax.conv_general_dilated(x, k, (1,1), "SAME", dimension_numbers=("NCHW","OIHW","NCHW"))
print(y.sum())