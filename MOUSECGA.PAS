program MouseCGA;
{demo to test mouse control in CGA graphic mode}
uses Dos, Graph;

type mouse_info = record
                    x, y: Integer;
                    button1, button2: Boolean
                  end;

var graph_driver, graph_mode, x: Integer;
    y, i: Byte;
    mouse: mouse_info;


function file_to_ptr(filename: string): Pointer;
{load a binary file to RAM and return a pointer to it}
var bin_file: File;
    size: Word;
    P: Pointer;

    begin Assign(bin_file, filename);
    Reset(bin_file, 1);

    size := FileSize(bin_file);
    GetMem(P, size);
    file_to_ptr := P;

    BlockRead(bin_file, P^, size);
    Close(bin_file) end;


procedure show_mouse;
var R: Registers;

    begin R.AX := 1;
    Intr($33, R) end;


procedure hide_mouse;
var R: Registers;

    begin R.AX := 2;
    Intr($33, R) end;


procedure init_mouse;
var R: Registers;
    P: Pointer;    

    begin R.AX := 0;    {initialize mouse driver}
    Intr($33, R);

    R.AX := 9;    {define own mouse cursor}
    R.BX := 7;    {horizontal hot spot}
    R.CX := 7;    {vertical hot spot}

    {P := file_to_ptr('CROSS.CUR');}       {cursor always white}
    P := file_to_ptr('CROSSXOR.CUR');    {cursor XORed on background}
    R.ES := Seg(P^);
    R.DX := Ofs(P^);
    Intr($33, R);

    show_mouse end;


procedure get_mouse_state;
var R: Registers;

    begin R.AX := 3;    {query mouse state}
    Intr($33, R);
    mouse.x := R.CX div 2;    {value in CX is always 0..639}
    mouse.y := R.DX;          {value in DX is always 0..199}
    mouse.button1 := (R.BX and 1) <> 0;
    mouse.button2 := (R.BX and 2) <> 0 end;


function to_string(number: Word): string;
var s: string;

    begin Str(number, s);
    to_string := s end;


begin
graph_driver := CGA;
graph_mode := CGAC3;
InitGraph(graph_driver, graph_mode, '');

for i := 3 downto 0 do begin
    SetFillStyle(SolidFill, i);
    Bar(60 + 60*i, 80, 80 + 60*i, 120);
    SetColor(1 + i mod 2);
    Rectangle(60 + 60*i, 80, 80 + 60*i, 120) end;

OutTextXY(160, 184, 'right click to exit');

init_mouse;

repeat
    get_mouse_state;
    if (mouse.x <> x) or (mouse.y <> y) then begin
        x := mouse.x;
        y := mouse.y;
        Bar(8, 8, 72, 15);
        OutTextXY(8, 8, to_string(x) + ', ' + to_string(y)) end;
    if mouse.button1 then begin
        hide_mouse;
        for i := 1 to 3 do begin
            SetColor(4 - i);
            Circle(mouse.x, mouse.y, 3*i) end;
        show_mouse end
    until mouse.button2

end.
