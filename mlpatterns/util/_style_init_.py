# style init
def align_tables(alignment='default'):
    from IPython.core.display import HTML

    match alignment:
        case 'left':
            talign = 'margin-left:0;margin-right:auto;'
        case 'right':
            talign = 'margin-left:auto;margin-right:0;'
        case 'center' | 'default' | 'reset' | '':
            talign = 'margin-left:auto;margin-right:auto;'
            
    table_css = '.rendered_html table{' + talign + '} '
    return HTML('<style>{}</style>'.format(table_css))

def align_output_tables(alignment='default'):
    from IPython.core.display import HTML

    match alignment:
        case 'center':
            talign = 'margin-left:auto;margin-right:auto;'
        case 'right':
            talign = 'margin-left:auto;margin-right:0;'
        case 'left' | 'default' | 'reset' | '':
            talign = 'margin-left:0;margin-right:auto;'
            
    table_css = 'div.output_area .rendered_html table{' + talign + '} '
    return HTML('<style>{}</style>'.format(table_css))
