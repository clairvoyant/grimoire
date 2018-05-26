{$mode objfpc}
{$h+}

program AppProgram;

uses custapp,classes;

const
  ShortOpts = 'hi:o:';
  LongOpts :  string = 'help input: output:';

type
  TApp = class(TCustomApplication)
    procedure DoRun ; Override;

    procedure PrintOptions;
  end;



procedure Usage;
begin
  WriteLn('app [--input=FILE] [--output=FILE] [--help]');
end;

{****************************************************
 *
 * Check Command line options
 *
 * CheckOptions returns default options and non default options. 
 *   FN: non parametric options
 *   Args: parametric options.
 ****************************************************}
 
procedure TApp.PrintOPtions;
var 
  E: string;
begin
    E := CheckOptions(ShortOpts, LongOpts);
    if E<> '' then
        WriteLn('error: ', E);

    if HasOption('i', 'input') then
        WriteLn('input file: ', GetOptionValue('i', 'input'));
    if HasOption('o', 'output') then
        WriteLn('output file: ', GetOptionValue('o', 'output'));
    if HasOption('h', 'help') then
        Usage;

  // Other way.... S:=CheckOptions(ShortOpts, Opts, Args, FN);

end;

{****************************************************
 * Initialization callback.
 *
 * Check parameters
 * print help
 *
 ****************************************************}
procedure TApp.DoRun;
begin

  PrintOptions;

  Terminate;
end;

{****************************************************
* Main program
 ****************************************************}
var
  App : TApp;
begin
  App:=TApp.Create(Nil);
  App.Initialize;
  App.Title:='Application Template';
  App.Run;
  App.Free;
end.
