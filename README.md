# Tourmaline

## Install

1) Virtual environment
Prepare a virtual environment for the tourmaline django project.
```bash
python3 -m venv venv
```
```bash
venv/bin/python -m ensurepip
venv/bin/python -m pip install --upgrade pip setuptools wheel
venv/bin/python -m pip install -r requirements.txt
```

2) LaTex integration
A macro is predefined in `config/extentions/tex_math.py` and pregestired in `settings.py` (`WIKI_MACRO = []`). 
The only remaining thing to do to make LaTex available in your wiki posts is to integrate the following script in the `<head>` 
of your default html template in `venv/lib/python3.13/site-packages/wiki/templates/wiki/base_site.html`. 
You can find it by using the command find `venv/ -name "base_site.html" | grep "wiki/templates/wiki"`. 

```html
<head>
<script>
    MathJax = {
        tex: {
            inlineMath: [['$$','$$'], ['\\(','\\)']]
        },
        svg: {
            fontCache: 'global'
        }
    };
</script>
<script type="text/javascript" id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
</script>
</head>
```

Use `'$$','$$'` or `['\\(','\\)']]` to call MathJax in your wiki post.

