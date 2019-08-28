procedure init_mouse;
var R: Registers;

    begin R.AX := 0;     {init mouse}
    Intr($33, R);

    R.AX := 7;     {min. & max. horizontal position}
    R.CX := 0;
    R.DX := 614;
    Intr($33, R);

    R.AX := 8;     {min. & max. vertical position}
    R.CX := 0;
    R.DX := 190;
    Intr($33, R) end;


procedure get_mouse_state;
var R: Registers;

    begin R.AX := 3;    {query mouse state}
    Intr($33, R);

    mouse.x := R.CX shr 1;    {convert 0..639 to 0..319}
    mouse.y := R.DX;
    mouse.left := (R.BX and 1) <> 0;
    mouse.right := (R.BX and 2) <> 0 end;


procedure show_mouse;

    begin mx := mouse.x;
    my := mouse.y;
    PutImage(mx, my, @RUKA^, XORPut) end;


procedure hide_mouse;

    begin PutImage(mx, my, @RUKA^, XORPut) end;


procedure wait_for_release;
{wait till no mouse button or key is pressed}
var R: Registers;
    key: Char;

    begin
    repeat
        R.AX := 3;
        Intr($33, R)
        until (R.BX and 3) = 0;
    while KeyPressed do
        key := ReadKey end;
