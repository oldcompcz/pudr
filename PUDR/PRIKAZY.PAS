function last_command: PCommand;
var result: PCommand;

    begin result := cmd_start;
    while result^.next <> nil do
        result := result^.next;

    last_command := result end;


procedure add_command(x: Word; y, fg, bg: Byte; type_of, name: string;
                      action, target: Shortint; thing: Shortint);
var x2: Word;
    y2, space: Byte;
    region: rectangle_region;
    prep: string[6];
    new_cmd: PCommand;

    begin New(new_cmd);
    new_cmd^.name := name;
    new_cmd^.action := action;
    new_cmd^.target := target;
    new_cmd^.next := nil;

    if cmd_start = nil then
        cmd_start := new_cmd
    else
        last_command^.next := new_cmd;

    region[left] := x;
    region[top] := y;

    if type_of = 'text' then begin
        space := Pos('!'{space}, name);
        prep := Copy(name, 1, space);
        name := Copy(name, space + 1, 10);

        {add arrows indicating movement along corridor}
        if (target in [10..18]) and (room in [10..18]) then
            if target < room then
                Insert('!!!'#27, prep, 3)
            else
                Insert('!!!'#26, prep, 3);

        x2 := x + 8*Length(name) + 3;
        y2 := y + 28;

        {display text command}
        SetFillStyle(SolidFill, bg);
        Bar(x, y, x2, y2);
        PutPixel(x + 1, y + 1, 3 - bg);
        PutPixel(x2 - 1, y + 1, 3 - bg);
        PutPixel(x + 1, y2 - 1, 3 - bg);
        PutPixel(x2 - 1, y2 - 1, 3 - bg);
        SetColor(fg);
        SetTextJustify(LeftText, TopText);
        decode_and_write(x + 3, y + 7, prep);
        decode_and_write(x + 3, y + 17, name);
        if action >= 0 then
            Line(x + 3, y + 25, x + 9, y + 25);
        {x_pos is global, shared with set_clickables and between calls to add_command}
        x_pos := x2 end

    else begin
        x2 := x + 37;
        y2 := y + 33 end;

    region[right] := x2;
    region[bottom] := y2;
    new_cmd^.region := region end;


procedure remove_last_command;
var cmd, last: PCommand;

    begin cmd := cmd_start;
    last := last_command;
    while cmd^.next <> last do
        cmd := cmd^.next;
    cmd^.next := nil;
    Dispose(last) end;


procedure clear_clickables;
    begin
    while last_command <> main_commands[5] do
        remove_last_command end;


procedure set_clickables(type_of: string);
var i, inv_slot: Byte;
    exits, exit_name: string;

    begin
    clear_clickables;

    if type_of = 'things' then begin

        for i := 0 to thing_count do
            {things in room}
            if (things[i].where = room) then
                if ((action <> 2) or things[i].portable)           {only portable things can be taken}
                        and ((action <> 2) or not inventory_full)  {& can be taken if inventory not full}
                        and (action <> 3)                          {& only owned things can be used}
                        and ((action <> 4) or (i in openables))    {& only some things make sense to open}
                        then
                    add_command(103 + 38*things[i].slot, 12,
                                0, 0, 'image', things[i].name, -1, i, i)
                else begin {dangling else} end

            {things in inventory}
            else if (things[i].where = 50) then
                if (action <> 2)                                   {owned things can't be taken}
                        and ((action <> 4) or (i in openables))    {& only some things make sense to open}
                        then begin
                    inv_slot := 0;
                    while inventory[inv_slot] <> i do
                        Inc(inv_slot);
                    add_command(41 + 40*inv_slot, 128,
                                0, 0, 'image', things[i].name, -1, i, i) end end

    else if type_of = 'exits' then begin
        {x_pos is global, shared with add_command}
        x_pos := 155;

        {first pass: get correct x_pos for a centered display}
        exits := room_exits[room];
        for i := 1 to Length(exits) do begin
            destination := Ord(exits[i]) - 48;
            exit_name := exit_names[destination];
            exit_name := Copy(exit_name, Pos('!'{space}, exit_name) + 1, 10);
            x_pos := x_pos - 4*Length(exit_name) - 3 end;

        {second pass: display commands}
        for i := 1 to Length(exits) do begin
            destination := Ord(exits[i]) - 48;
            add_command(x_pos + 5, 79, 3 - i, i, 'text',
                        exit_names[destination], -1, destination, -1) end end

    else
        add_command(130, 79, 0, 3, 'text', texts_short[8]{Odejit do DOSu}, -1, 0, -1) end;


function get_clicked_command: PCommand;
var result: PCommand;

    begin result := cmd_start;
    while result <> nil do begin
        if (result^.region[left] <= mouse.x) and (mouse.x <= result^.region[right])
                and (result^.region[top] <= mouse.y) and (mouse.y <= result^.region[bottom]) then
            Break;
        result := result^.next end;

    get_clicked_command := result end;
