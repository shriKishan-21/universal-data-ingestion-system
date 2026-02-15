# What is __init__.py?
# __init__.py tells Python that a folder should be treated as a package.

# In simple words:
# Folder without __init__.py → just a folder
# Folder with __init__.py → Python package


# What Happens WITHOUT __init__.py?
# If you try:

# from src.loader import load_data

# Python may say:
# ModuleNotFoundError: No module named 'src'


# Because Python thinks:
# “src is just a normal folder, not importable.”