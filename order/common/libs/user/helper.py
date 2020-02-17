from flask import g,render_template

#统一模版化

def g_render_template(template,context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    
    return render_template(template,**context)