# import jax, jax.numpy as jnp
# print(jax.devices())
# x = jnp.ones((64, 19, 11, 11))
# k = jnp.ones((32, 19, 5, 5))
# y = jax.lax.conv_general_dilated(x, k, (1,1), "SAME", dimension_numbers=("NCHW","OIHW","NCHW"))
# print(y.sum())

import random

import wandb

# Start a new wandb run to track this script.
run = wandb.init(
    # Set the wandb entity where your project will be logged (generally your team name).
    entity="aadhi_44-independent-researcher",
    # Set the wandb project where this run will be logged.
    project="my-awesome-project",
    # Track hyperparameters and run metadata.
    config={
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    },
)

# Simulate training.
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2**-epoch - random.random() / epoch - offset
    loss = 2**-epoch + random.random() / epoch + offset

    # Log metrics to wandb.
    run.log({"acc": acc, "loss": loss})

# Finish the run and upload any remaining data.
run.finish()