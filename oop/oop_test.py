# %% [markdown]
# Import 3rd party http library: requests

# %%
import requests

# %% [markdown]
# http GET on httpbin.org endpoint. Save response in variable ***resp***

# %%
resp = requests.get('http://httpbin.org/json')

# %% [markdown]
# Check if request went okay by inspecting status_code.

# %%
resp.status_code

# %% [markdown]
# Everything is an object

# %%
type(resp)

# %%
help(resp)

# %% [markdown]
# Convert payload to json! internally actually a dict

# %%
resp.json()

# %%
resp.headers

# %%
resp.content


