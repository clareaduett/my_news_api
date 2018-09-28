import click
import requests
'''
A command line application that consumes a NewsApi.
'''


@click.command()

@click.option('--News', is_flag=True, help="Will print News Articles.")
def cli():
    click.echo('Hello here')
    '''
    Please check this
    '''

    url=''

    get_data(url)
    get_new_sources()
    greet()
    draw_header()
        
def get_data(url):
    req = requests.get(url)
    data = req.json()
    return data   

def get_new_sources():
    cnn = get_data('https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=e5802db2c57b4720975aa08560bea8cb')
    al_jazeera = get_data('https://newsapi.org/v2/top-headlines?sources=al-jazeera-english&apiKey=e5802db2c57b4720975aa08560bea8cb')
    bbc = get_data('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=e5802db2c57b4720975aa08560bea8cb')
    cbs = get_data('https://newsapi.org/v2/top-headlines?sources=cbs-news&apiKey=e5802db2c57b4720975aa08560bea8cb')
            
    chosen_source = []
    choices = {1: cnn['articles'][0:11],2:al_jazeera['articles'][0:11],3:bbc['articles'][0:11],4: cbs['articles'][0:11]}
            
    try:
        user_choice = input("enter 1 for cnn ,2 for al_jazeera,3 for bbc,2 for cbs \n \t")
        number = int(user_choice)
    except:
        click.echo("you did not enter a number")
        return get_new_sources()

    if number == 1:
        chosen_source.append(choices[1])
    elif number == 2:
        chosen_source.append(choices[2])
    elif number == 3:
        chosen_source.append(choices[3])
    elif number == 4:
        chosen_source.append(choices[4])
    else:
        click.echo("choose a number between 1,2,3 and 4")
        return get_new_sources()


    return chosen_source
final = get_new_sources()
click.echo(final)

def greet():
    click.echo('Hello!,welcome to cled your CLI.')
    user_name=input('>What\'s your name?: ')
    click.echo('\nHey {},Thank you for chosing Cled as your trusted news source \n'.format(user_name))
    click.echo('-' * 100)

def draw_header():
    click.echo('\n') 
    click.echo(click.style('-' * 100, fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 32 + 'WELCOME TO CLED' + ' ' * 32 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='green'))
    click.echo(click.style('*' * 100, fg='green'))
    click.echo('\n')
