import click


@click.command()
@click.option('--name', default='World' ,help='Name of the person')
@click.option('--repeat', default=1, type = int, help="Number of times to repeat")
@click.option('--age', type = int, help='Age of the person')
@click.argument('out', type = click.File('w'), default = '-', required = False) #click type, arguments cannot have help message
def cli(name, repeat, age, out):
    """This scripts greets you"""
    #click.echo(out)
    
    for x in range(repeat):
        click.echo("Hello {}, you are {}".format(name, age), file=out)

