import typer

app = typer.Typer()

@app.command() #decorator
def hello(name: str, age: int, display_age: bool = True):
    if display_age:
        print("Hello {}, you are {}".format(name, age))
    else:
        print("Hello {}!".format(name, age))

@app.command() #decorator
def goodbye():
    print("GoodBye")

if __name__ == '__main__':
    app()