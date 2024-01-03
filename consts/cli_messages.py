from core_script.cli_formatters import bold, red, green


no_api_keys_message = bold(red('''
*******************************************************************
***                You do not have any API keys.                ***
***     Please procure keys and store them in .env root file    ***
*******************************************************************
'''))

not_ready_warning_message = bold(red('''
\n*******************************************************************
***                          WARNING                            ***
***              The script is NOT ready to trade               ***
***        Please do not use 'prod_dangerous' param yet         ***
*******************************************************************
'''))

help_message = f'''
{green('COMMANDS')}

Modify the scripts execution behavior by adding params
after calling the script. No need to add additional syntax, 
just the word will do.

Available script run modes:
... {green('test')} [default]   => runs script in paper trading, skipping certain account checks
... {green('full_test')}        => runs script in paper trading, including account checks
... {green('prod')}             => runs script with real trading account
... {green('prod_dangerous')}   => runs script with real money and trading authorization
... {green('download')}         => runs script with paper creds and initials a download of the data
... {green('help')}             => shows help command
\033[0m
'''

hl = '\n*******************************************************************\n'