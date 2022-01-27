import click

class Config(object):
    def __init__(self):
        self.verbose = False
        self.home_directory = None


pass_config = click.make_pass_decorator(Config, ensure = True)

@click.group() #any group can have sub commands
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type = click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory
    


#Sub command 1
@cli.command()
@click.option('--name', default='World' ,help='Name of the person')
@click.option('--repeat', default=1, type = int, help="Number of times to repeat")
@click.option('--age', type = int, help='Age of the person')
@click.argument('out', type = click.File('w'), default = '-', required = False) #click type, arguments cannot have help message
@pass_config
def say(config, name, repeat, age, out):
    """This scripts greets you"""
    #click.echo(out)
    if config.verbose:
        print("We are in verbose mode")
    click.echo('Home directory is {}'.format(config.home_directory))
    for x in range(repeat):
        click.echo("Hello {}, you are {}".format(name, age), file=out)

#Sub command 2
@cli.command()    
@click.option('--AAA', default='World' ,help='')
@pass_config
def foo(config, AAA):
    """This is the foo command 
        Second line but is not working :D
    """
    click.echo("Hello {}".format(AAA))

    #https://www.youtube.com/watch?v=kNke39OZ2k0