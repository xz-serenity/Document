# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'docs'
copyright = '2024, Sean Xiao'
author = 'Sean Xiao'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
   # 'numpydoc',
   'myst_parser',
   'sphinx.ext.duration',
   'sphinx.ext.autodoc',
   'sphinx.ext.napoleon',
   'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

# 配置 copybutton 的行为, 设置不复制代码块前的提示符（如 ">>>", "$" 等）
copybutton_prompt_text = r">>> |\$ "  # 正则表达式匹配提示符
copybutton_only_copy_prompt_lines = False  # 如果提示符匹配，是否只复制带提示符的行

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
