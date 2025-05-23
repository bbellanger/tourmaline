from wiki.plugins.macros import settings, register

@register
def tex_math(macro, arg_string, page, context):
    return f"$$ {arg_string.strip()} $$"
