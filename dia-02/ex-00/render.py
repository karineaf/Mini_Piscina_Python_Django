import sys
import re


def create_HTML_from_template():
              
    template_file = get_template_from_args()
    html_name = template_file.name.replace('.template','')    
    html = open(f'{html_name}.html', "w")
    init_html(html)
    
    if template_file:
        for line in template_file:
            pattern = "{(\w+)}"
            attributes = re.findall(pattern, line)
            for attribute_key in attributes:
                formatted_attribute_key = "{" + attribute_key + "}"
                attribute_value = globals()[attribute_key]
                line = line.replace(formatted_attribute_key, str(attribute_value))
            html.write(line)       
    
    close_html(html)   


def get_template_from_args():
    try:
        template = sys.argv[1]
        if len(sys.argv) != 2:
            raise Exception() 
        if ".template" in template:
            return open(template, "r")
        else:
            raise TypeError() 
    except IndexError:
        print('No template file was reported!')
    except FileNotFoundError:
        print('File not found!')
    except TypeError:
        print('Wrong file extension!') 
    except Exception:
        print("Wrong number of arguments!") 
                   
def init_html(html):
    
    html.write('''
<!DOCTYPE html >
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CV</title>
</head>
<body>''')

def close_html(html):
    html.write("</body>")
    html.close()


if __name__ == "__main__":
    exec(open("settings.py", "r").read()) 
    create_HTML_from_template()