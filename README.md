# click-fish
Fish completion for Click

Add automatic completion support for [fish](https://fishshell.com) to
[Click](http://click.pocoo.org)

## Usage

Just

    import click_fish

in your Click script.

## Activation

In order to activate Fish completion, you need to inform Fish that completion is
available for your script, and how. Any Click application automatically provides
support for that. The general way this works is through a magic environment
variable called `_<PROG_NAME>_COMPLETE`, where `<PROG_NAME>` is your application
executable name in uppercase with dashes replaced by underscores.

If your tool is called foo-bar, then the magic variable is called
`_FOO_BAR_COMPLETE`. By exporting it with the source value it will spit out the
activation script which can be trivally activated.

For instance, to enable Fish completion for your foo-bar script, this is what
you would need to put into your ~/.config/fish/completions/foo-bar.fish

    eval (_FOO_BAR_COMPLETE=source-fish foo-bar)

From this point onwards, your script will have Fish completion enabled.

## Activation Script

The above activation example will always invoke your application on startup.
This might be slowing down the shell activation time significantly if you have
many applications. Alternatively, you could also ship a file with the contents
of that, which is what Git and other systems are doing.

This can be easily accomplished:

    _FOO_BAR_COMPLETE=source-fish foo-bar > ~/.config/fish/completions/foo-bar.fish

## License

Licensed under the MIT, see LICENSE.
